# Image Captioning with CNN-RNN

This project demonstrates how to generate natural language captions for images using a Convolutional Neural Network (CNN) encoder and a Recurrent Neural Network (RNN) decoder. The model was trained on the Microsoft COCO 2014 dataset using PyTorch.

Originally completed as part of Udacity's Computer Vision Nanodegree.

---

## Project Overview

- **Encoder**: Pretrained ResNet-18 to extract image features  
- **Decoder**: LSTM network that generates captions from image embeddings  
- **Training**: COCO 2014 dataset (subset of ~2,000 images)  
- **Evaluation**: Greedy decoding vs. Beam search (beam width = 5)

---

## Example Outputs

| Input Image     | Predicted Caption                                         |
|------------------|-----------------------------------------------------------|
| White Boat       | "a boat is on the water with trees in the background"     |
| Giraffe (Error)  | "a giraffe standing under a roof" *(incorrect)*           |

---

## Key Learnings

- Built a CNN-RNN pipeline for sequence generation
- Extracted features using a pretrained CNN
- Generated captions using beam search decoding
- Explored overfitting and diversity in language models

---

## Files

| File                        | Description                                        |
|-----------------------------|----------------------------------------------------|
| `image_captioning_cnn_rnn.ipynb` | Final notebook (training, inference, analysis)   |
| `model.py`                  | EncoderCNN and DecoderRNN classes                  |
| `data_loader.py`            | COCO dataset loader and preprocessing              |
| `images/`                   | Screenshots and example caption outputs            |
| `README.md`                 | Project overview and instructions                  |

---

## Getting Started

To run the notebook locally:

1. Clone the repository  
2. Install dependencies: `torch`, `torchvision`, `matplotlib`, `nltk`, etc.  
3. Open `image_captioning_cnn_rnn.ipynb` using Jupyter or Colab  
4. (Optional) Download and preprocess the COCO 2014 dataset  

**Note**: COCO images and trained model weights are not included due to licensing restrictions.

---

## Contact

Feel free to reach out or connect:

- **LinkedIn** – [Crystal Ford](https://www.linkedin.com/in/crystalmford)  
- **GitHub** – [@crystalmford](https://github.com/crystalmford)

---


---

## Contact

If you’re hiring or would like to collaborate, please connect with me on [LinkedIn](https://www.linkedin.com/in/crystal-m-ford/).
