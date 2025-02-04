# Arabic Text Correction

This repository provides tools and resources for developing Arabic text correction models utilizing the QALB-2014-L1 dataset. This dataset is essential for Natural Language Processing (NLP) research, containing annotated Arabic texts that highlight common grammatical errors, making it ideal for training and evaluating correction algorithms.

## Table of Contents

- [Introduction](#introduction)
- [Literature Review](#Literature Review)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributors](#contributors)

## Introduction
Arabic, with its [rich morphology](https://discuss.huggingface.co/t/mrls-morphologically-rich-languages-nlp/3868/2) and complex syntax, presents unique challenges in text correction tasks. The presence of diacritics, word inflections, and context-dependent meanings further complicates the process of detecting and correcting errors. These complexities highlight the need for specialized approaches to effectively handle Arabic text.

Our project focuses on Arabic text correction, leveraging the QALB-2014-L1 dataset to develop robust models capable of identifying and correcting grammatical errors, restoring diacritics, and resolving common linguistic issues. By addressing these challenges, our work aims to enhance the quality and accuracy of Arabic text processing, supporting applications in education, automated proofreading, and content generation.

## Literature Review
[Leveraging Part-of-Speech Tagging for Robust Arabic Text Correction.pdf](https://github.com/user-attachments/files/18654240/Leveraging.Part-of-Speech.Tagging.for.Robust.Arabic.Text.Correction.pdf)


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

## Usage  
The repository includes scripts for data preprocessing, model training, and evaluation. Detailed instructions for each step are provided below. 


## Model Training
### MLE:
Maximum Likelihood Estimation (MLE) is a statistical method used to estimate the parameters of a model by maximizing the likelihood of the observed data. In the context of Arabic text correction with bigrams, We used MLE to determine the most likely sequence of words or corrections based on probabilities derived from the training.

### AraT5:
AraT5 is a model specifically designed for handling Arabic language processing tasks, built on the T5 architecture. It supports various NLP applications such as text generation, translation, question generation, and paraphrasing in Arabic. Beyond its pre-built capabilities, we use it for the QALB-2014 Dataset to fine-tuned for to improves the performance of GEC for more information about AraT5 click on the [link](https://github.com/UBC-NLP/araT5). 

### AraT5 + POS:
AraT5v2 with POS improves error correction by adding Part-of-Speech (POS) tagging to the input. It uses POS tags from Stanza to give the model more grammatical and structural context. 

This helps the model better understand sentence structure and grammar, leading to more accurate corrections. It also speeds up training and improves performance. Tests on the QALB-2014 dataset show that this approach performs better than the standard AraT5v2 model.
## Contributors
This project is a collaborative effort by the following contributors:

[Sultan Masoud Alaqili](https://github.com/SL6I)  
[Naif Muteb Alharbi](https://github.com/Naif901)  
[Mohammed Ahmed Almufarriji](https://github.com/Mohammedamd12)  
[Mohammed Abdullah Saati](https://github.com/MohammedSaati)

   
  
