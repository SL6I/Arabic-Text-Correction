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
![image alt](https://github.com/SL6I/Text-Correction/blob/5ea1f014c9f4d6cc7953e35c2093622309d23c42/Sample%20Train%20Data.jpg)
### Validation Data Sample
![image alt](https://github.com/SL6I/Text-Correction/blob/5ea1f014c9f4d6cc7953e35c2093622309d23c42/Sample%20Dev%20Data.jpg)
### Testing Data Sample
![image alt](https://github.com/SL6I/Text-Correction/blob/5ea1f014c9f4d6cc7953e35c2093622309d23c42/Sample%20Test%20Data.jpg)

## Data Access
To access the datasets for training, validation, and testing, use the following links:
- Training Data: [Click To Download](https://drive.google.com/file/d/1EQuXoM3Tj5bZqsZxYBakhZ7ZNbFH-1LB/view?usp=drive_link)
- Validation Data: [Click To Download]()
- Testing Data: [Click To Download]()
