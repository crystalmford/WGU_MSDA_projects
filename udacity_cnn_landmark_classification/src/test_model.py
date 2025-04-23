import torch
from src.model import MyModel
from src.optimization import get_loss
from src.data import get_data_loaders
from train import one_epoch_test

# Choose device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Instantiate the model
model = MyModel(num_classes=50)
model.load_state_dict(torch.load("checkpoints/best_val_loss.pt"))
model.to(device)
model.eval()

# Get loss function
loss_fn = get_loss()

# Load the test data
data_loaders = get_data_loaders(batch_size=50, limit=200, valid_size=0.5, num_workers=0)
test_loader = data_loaders["test"]

# Run testing
one_epoch_test(test_loader, model, loss_fn)
