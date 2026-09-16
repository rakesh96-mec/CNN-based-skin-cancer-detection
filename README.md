# Portable Skin Lesion Classification Device Using CNN

An academic **B.E. Mechatronics Engineering team project (2021–2022)** exploring a portable image-based system for classifying skin lesions using a Convolutional Neural Network (CNN).

The original project combined a camera, Raspberry Pi, display, machine-learning inference and a user-facing interface to provide a portable prototype for skin-lesion classification.

> **Academic project:** developed as part of a four-member B.E. Mechatronics Engineering team.

## Project Overview

The system was designed around the following workflow:

```text
Camera / Image Input
        ↓
Raspberry Pi
        ↓
Image Pre-processing
        ↓
CNN Classification
        ↓
Predicted Lesion Category
        ↓
Result Display
```

The project report describes a portable device using a **Raspberry Pi 3B+**, a **5 MP camera module**, and a **capacitive touch display**. The intended workflow allowed the user to select or capture an image, submit it for evaluation, and view the resulting category on the interface.

## Classification

The CNN was developed to classify images into seven lesion categories:

| Class | Category |
|---|---|
| 0 | Actinic Keratosis |
| 1 | Basal Cell Carcinoma (BCC) |
| 2 | Benign Keratosis |
| 3 | Dermatofibroma |
| 4 | Melanoma |
| 5 | Melanocytic Nevus |
| 6 | Vascular Lesion |

## CNN Model

The preserved training code:

- Loads HAM10000 metadata.
- Encodes the diagnostic classes.
- Balances the seven classes for model development.
- Resizes input images to **32 × 32 pixels**.
- Normalizes pixel values to the 0–1 range.
- Uses a CNN with three convolution/max-pooling stages and dropout.
- Uses a seven-class softmax output layer.
- Trains using categorical cross-entropy and Adam.
- Evaluates the model and generates training/validation plots and a confusion matrix.

The current training script uses **500 samples per class** for the balanced training dataset before the train/test split.

## Datasets

The academic project documentation identifies **HAM10000** and the **ISIC archive** as the principal image sources used in the project.

The datasets are not included in this repository.

Refer to the original datasets and their respective terms of use before downloading or redistributing any medical images.

## Hardware

The original prototype was designed around:

- Raspberry Pi 3B+
- 5 MP camera module
- Capacitive touch display
- Micro SD storage
- Supporting electronics and enclosure

The project report describes the physical prototype as a portable device intended for image acquisition, local processing and result presentation.

## Software & Technologies

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- OpenCV / image processing
- Matplotlib
- Seaborn
- Scikit-learn
- Raspberry Pi
- Flask
- AWS cloud services

## Training and Evaluation

The preserved training implementation performs:

```text
Dataset Metadata
      ↓
Class Encoding
      ↓
Class Balancing
      ↓
Image Resize / Normalization
      ↓
Train / Test Split
      ↓
CNN Training
      ↓
Model Evaluation
      ↓
Confusion Matrix
```

The project report records the following evaluation results from the developed prototype:

- **92% accuracy** on clinically captured images
- **approximately 60% accuracy** on normally captured images

These values are reported results from the original academic project and are not presented here as a current clinical benchmark.

## Inference

The repository contains an inference workflow that:

1. Loads the trained CNN model.
2. Accepts an input image.
3. Resizes the image to 32 × 32 pixels.
4. Normalizes pixel values.
5. Runs CNN inference.
6. Selects the predicted class.
7. Maps the class index to the corresponding lesion category.

## Web Interface

The project also included a simple Flask-based interface for image submission and result presentation.

The original academic report describes a workflow in which the user can:

1. Select an image or capture one through a camera.
2. Submit the image.
3. Receive the predicted category and associated information.

## Repository Structure

```text
CNN-based-skin-cancer-detection/
│
├── cnn_model_training.py
├── cnn_skin_lesion_inference.py
├── flask_skin_lesion_app.py
├── projecttest1.py
├── skin_lesion_cnn_model.h5
├── types.json
├── requirements.txt
├── README.md
│
└── templates/
    └── SkinCancer.html
```

## Applications

The project explored potential applications in:

- Portable skin-lesion screening support
- Computer-aided image classification
- Edge/embedded machine-learning systems
- Accessible computer-vision-based healthcare prototypes

This project was developed as an academic prototype and should not be treated as a clinical diagnostic system.

## Limitations and Future Scope

The project documentation identifies several limitations, including the limited number of supported lesion categories, the effect of image quality on classification performance, and the need for larger and more diverse datasets.

Future development discussed in the project includes:

- Larger and more diverse training datasets
- Higher-resolution image acquisition
- Additional skin-condition categories
- Improved device design
- Additional clinical information as model inputs
- Continued collaboration with medical institutions for dataset development

## Project Context

**B.E. Mechatronics Engineering — Academic Team Project**  
The Oxford College of Engineering, Visvesvaraya Technological University (VTU), 2021–2022

**Team:** Sahana S R, Mahesh P S, Rakesh N R, Yugal Kishore R N

## Author

**Rakesh Nuggehalli Ramesh**

B.E. Mechatronics Engineering
