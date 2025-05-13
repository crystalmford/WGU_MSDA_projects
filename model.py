import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F


class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet18(pretrained=True)
        modules = list(resnet.children())[:-1]  # remove the last FC layer
        self.resnet = nn.Sequential(*modules)
        self.embed = nn.Linear(resnet.fc.in_features, embed_size)

    def forward(self, images):
        with torch.no_grad():
            features = self.resnet(images)
        features = features.view(features.size(0), -1)
        features = self.embed(features)
        return features


class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size):
        super(DecoderRNN, self).__init__()
        self.hidden_size = hidden_size
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, batch_first=True)
        self.linear = nn.Linear(hidden_size, vocab_size)

    def forward(self, features, captions):
        embeddings = self.embed(captions[:, :-1])  # exclude <end> token
        features = features.unsqueeze(1)
        inputs = torch.cat((features, embeddings), 1)
        hiddens, _ = self.lstm(inputs)
        outputs = self.linear(hiddens)
        return outputs

    def sample(self, features, states=None, max_len=20, start_token_id=None, end_token_id=None):
        """Generate a caption using greedy search."""
        output = []

        h0 = torch.zeros(1, 1, self.hidden_size).to(features.device)
        c0 = torch.zeros(1, 1, self.hidden_size).to(features.device)
        states = (h0, c0)

        if features.dim() == 2:
            inputs = features.unsqueeze(1)  # (1, 1, embed_size)
        else:
            inputs = features

        for _ in range(max_len):
            hiddens, states = self.lstm(inputs, states)
            outputs = self.linear(hiddens.squeeze(1))
            predicted = outputs.argmax(1)
            output.append(predicted.item())
            if end_token_id is not None and predicted.item() == end_token_id:
                break
            inputs = self.embed(predicted).unsqueeze(1)

        return output

    def sample_beam_search(self, features, states=None, max_len=20, start_token_id=None, end_token_id=None, beam_width=3):
        """Generate a caption using beam search."""
        device = features.device
        inputs = features.unsqueeze(1)  # (1, 1, embed_size)

        h0 = torch.zeros(1, 1, self.hidden_size).to(device)
        c0 = torch.zeros(1, 1, self.hidden_size).to(device)
        states = (h0, c0)

        beams = [(0.0, [start_token_id], states, inputs)]

        for _ in range(max_len):
            new_beams = []

            for score, seq, states, inputs in beams:
                hiddens, states = self.lstm(inputs, states)
                outputs = self.linear(hiddens.squeeze(1))
                probs = F.log_softmax(outputs, dim=1)

                topk_probs, topk_ids = torch.topk(probs, beam_width, dim=1)

                for i in range(beam_width):
                    word_id = topk_ids[0][i].item()
                    word_prob = topk_probs[0][i].item()

                    new_seq = seq + [word_id]
                    new_score = score + word_prob

                    if end_token_id is not None and word_id == end_token_id:
                        new_beams.append((new_score, new_seq, None, None))
                    else:
                        next_input = self.embed(topk_ids[0][i]).unsqueeze(0).unsqueeze(1)
                        new_beams.append((new_score, new_seq, states, next_input))

            beams = sorted(new_beams, key=lambda x: x[0], reverse=True)[:beam_width]

            if all((s is None or (len(seq) > 0 and seq[-1] == end_token_id)) for _, seq, s, _ in beams):
                break

        return beams[0][1]

