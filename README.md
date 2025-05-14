Image Generation with GANs
This project trains a Deep Convolutional GAN (DCGAN) to generate 64x64 pixel face images using a cropped version of the CelebA dataset. It was completed as part of the Udacity Deep Learning Nanodegree and demonstrates my ability to:

Build and train adversarial neural networks (GANs)

Customize data pipelines with PyTorch

Track model performance over time

Evaluate image generation quality and model limitations

Project Structure
image_generation_gan/
├── image_generation_gan.ipynb → Main notebook with training code and outputs
├── tests.py → Unit tests for generator, discriminator, and dataset
├── processed-celeba-small.zip → Optional: zipped data subset (CelebA 64x64)
├── processed_celeba_small/ → Required: unzipped dataset directory
├── generated_faces/ → Outputs: sample face grids saved each epoch
├── requirements.txt → Python package dependencies
├── assets/ → (Optional) Screenshots or saved visualizations
├── __MACOSX/ → Ignore (Mac unzip artifact)

How to Run This Project
Install dependencies

Run this command in your terminal:

pip install -r requirements.txt

Prepare the data

Unzip processed-celeba-small.zip if needed, and ensure the image data is located at:
processed_celeba_small/celeba/

Run the notebook

Open image_generation_gan.ipynb and run all cells in order. Sample images are saved to the generated_faces/ folder after each epoch.

Example Output
The model generates 4x4 image grids of fake celebrity faces from random noise vectors using a trained generator.

Check the generated_faces/ folder for images like:

epoch_01.png

epoch_10.png

epoch_35.png

These help visualize the GAN's progress over training.

Loss Curve
At the end of training, loss curves are plotted for both the generator and discriminator to help evaluate training stability.

Model Limitations
The CelebA dataset is biased toward young white celebrity faces. The model may not generalize well to diverse populations. Generated samples may also appear blurry or lack high-frequency detail.

Future Improvements
Train for more epochs

Use a deeper generator architecture

Try a different loss function (e.g., WGAN-GP)

Train on a more diverse dataset

Author
Crystal Ford
WGU MSDA | Deep Learning Student
GitHub Profile