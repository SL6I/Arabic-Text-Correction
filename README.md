# Arabic Text Correction

This repository provides tools and resources for developing Arabic text correction models utilizing the QALB-2014-L1 dataset. This dataset is essential for Natural Language Processing (NLP) research, containing annotated Arabic texts that highlight common grammatical errors, making it ideal for training and evaluating correction algorithms.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributors](#contributors)

## Introduction
Arabic, with its [rich morphology](https://discuss.huggingface.co/t/mrls-morphologically-rich-languages-nlp/3868/2) and complex syntax, presents unique challenges in text correction tasks. This project aims to address these challenges by leveraging the QALB-2014-L1 dataset to develop robust models capable of identifying and correcting grammatical errors in Arabic texts.  
ADD MORE TEXT

## Dataset  
The [QALB-2014-L1 dataset](https://github.com/SL6I/Text-Correction/blob/7b67fd25d517431ea77ced2d02754a0fb5977a8d/Dataset/Dataset.md) comprises native Arabic user comments from the Al Jazeera news website, annotated to highlight common grammatical errors. This dataset is instrumental in training models for grammatical error detection and correction in Arabic. 
## Installation
To set up the project locally:  

  
**Clone the repository:**  
   ```bash
   git clone https://github.com/SL6I/Text-Correction.git
   ```
**Install the required dependencies:**  
```bash
pip install -r requirements.txt
```
**(Optional) Navigate to the scripts folder:** 
```bash  
cd scripts
```
> [!TIP]
> Navigating to the scripts folder (cd scripts) is not strictly necessary, but it makes running the subsequent commands easier since you won’t need to include the folder path in each command.

## Usage  
The repository includes scripts for data preprocessing, model training, and evaluation. Detailed instructions for each step are provided below. 


## Model Training
### MLE

### ARAT5:
AraT5 is a model specifically designed for handling Arabic language processing tasks, built on the T5 architecture. It supports various NLP applications such as text generation, translation, question generation, and paraphrasing in Arabic. Beyond its pre-built capabilities, we use it for QALB-2014 Dataset to fine-tuned for to improves the performance of GEC 
## Contributors
This project is a collaborative effort by the following contributors:

[Sultan Masoud Alaqili](https://github.com/SL6I)  
[Naif Muteb Alharbi](https://github.com/Naif901)  
[Mohammed Ahmed Almufarriji](https://github.com/Mohammedamd12)  
[Mohammed Abdullah Saati](https://github.com/MohammedSaati)

   
  
