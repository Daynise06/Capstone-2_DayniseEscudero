![](UTA-DataScience-Logo(1).png)


# 🫁 CardioScan AI: Deep Learning for Cardiomegaly Detection

* **One Sentence Summary:** This repository implements a DenseNet121 architecture to detect Cardiomegaly in Chest X-rays using a balanced subset of the NIH Chest X-ray dataset.


## 📌 Overview
* Definition of Task: The challenge is to perform binary image classification on Chest X-rays to identify Cardiomegaly (heart enlargement). Early detection is critical as it is a primary indicator of congestive heart failure.

* Your Approach: We formulated this as a supervised computer vision task. We utilized Transfer Learning with a DenseNet121 model, pre-trained on ImageNet, to extract complex features from medical scans. The final layers were tuned specifically for cardiothoracic ratio analysis.

* Summary of Performance: Our best model achieved a confidence level of approximately 98% on positive cases. The deployment was built using Streamlit to bridge the gap between AI modeling and clinical usability.

## 📊 Summary of Work Done
### Data
* Type: 5,552 Chest X-ray images (PA view) in PNG/JPEG format.

* Input: 224x224 RGB pixel arrays.

* Output: Binary labels (0: Healthy, 1: Cardiomegaly).

* Split: 80% Training, 10% Validation, 10% Testing.

### Preprocessing
* Resized images to 224x224 pixels for DenseNet compatibility.

* Applied Normalization using ImageNet mean and standard deviation.

* Implemented Data Augmentation (horizontal flips and rotations) to prevent overfitting.

### Training
* Software: Python, PyTorch, Google Colab (with A100/T4 GPU).

* Optimizer: Adam Optimizer with a learning rate of 0.0001.

* Loss Function: Binary Cross-Entropy with Logits (BCEWithLogitsLoss).

* Difficulty: Imbalanced datasets are common in medical imaging; we resolved this by using a balanced sample of 5,552 images.
