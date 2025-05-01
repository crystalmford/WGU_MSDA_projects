# Landmark Image Classification using CNNs

This project implements a deep learning pipeline to classify images of 50 global landmarks using PyTorch. It includes both a custom Convolutional Neural Network (CNN) and a transfer learning model using ResNet18. The final model is deployed in a simple interactive app.

---

## Project Overview

The goal is to predict which landmark is depicted in a given photograph. The project is organized into three Jupyter notebooks:

| Notebook                                   | Description |
|--------------------------------------------|-------------|
| `cnn_from_scratch_landmark_classifier.ipynb` | Build and train a CNN from scratch. |
| `transfer_learning_landmark_classifier.ipynb` | Improve accuracy with a pretrained ResNet18 model. |
| `app_landmark_classifier.ipynb`            | Classify user-uploaded images using the exported model. |

---

## Key Results

| Model                     | Final Test Accuracy |
|---------------------------|---------------------|
| CNN from Scratch          | ~35%                |
| Transfer Learning (ResNet18) | 76.4%               |

The best-performing model was exported using TorchScript and saved to:
`checkpoints/transfer_exported.pt`

---

## Setup & Requirements

Install dependencies:

    pip install -r requirements.txt

To run the notebooks:

- Use Jupyter Notebook or Jupyter Lab
- Make sure PyTorch, torchvision, and ipywidgets are installed

---

## Dataset

The dataset is a subset of the Google Landmarks Dataset v2. It is not included in this repo due to size. To reproduce training, place the dataset in a folder named `landmark_images/` in the root directory.

---

## Highlights

- End-to-end model training from scratch and with transfer learning
- Modularized pipeline in the `src/` directory
- TorchScript export for easy deployment
- Interactive app for classifying images

---

## Project Structure

    udacity_cnn_landmark_classification/
    ├── cnn_from_scratch_landmark_classifier.ipynb
    ├── transfer_learning_landmark_classifier.ipynb
    ├── app_landmark_classifier.ipynb
    ├── requirements.txt
    ├── README.md
    ├── checkpoints/          # .gitignored
    ├── static_images/        # .gitignored
    ├── landmark_images/      # .gitignored
    └── src/                  # source code modules

---

Built with PyTorch and Jupyter.


