# Dataset Overview

## Source
This dataset has been curated specifically for the purpose of Arabic text correction. It is part of the [AraSpell project](https://github.com/msalhab96/AraSpell/blob/main/README.md), which aims to improve the quality of text processing in the Arabic language.

## Dataset Contents
- `train.csv`: Used for training the model. Contains 6,922,318 rows and 5 columns (97.19%).
- `dev.csv`: Used for validating model performance during the training phase. Contains 100000 rows and 5 columns (1.40%).
- `test.csv`: Used for final testing and evaluation of the model. Contains 100000 rows and 5 columns (1.40%).

## Columns and Features
- `Unnamed: 0`: Index column for each record in the dataset.
- `Clean`: Original Arabic text, serving as the reference for corrections.
- `Distorted_0.05`: Text with minor 5% distortions from the original.
- `Distorted_0.1`: Text with moderate 10% distortions from the original.
- `Distorted_0.15`: Text with significant 15% distortions from the original.

## Sample Data
### Training Data Sample
![image alt](https://github.com/SL6I/Text-Correction/blob/082c557927b8069459b392e0cc0a63e3e4d36c88/Sample%20Data.jpg)
### Validation Data Sample

### Testing Data Sample

## Data Access
To access the datasets for training, validation, and testing, use the following links (if hosted externally):

Training Data: [Download Train Dataset]
Validation Data: [Download Dev Dataset]
Testing Data: [Download Test Datase]
