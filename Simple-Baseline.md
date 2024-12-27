# Simple-Baseline: Sample Approach to Text Correction

## Introduction
This document provides a **simple baseline** approach for text correction using [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) and evaluates its effectiveness using standard metrics such as **precision**, **recall**, and **F1-score**. The methodology follows a structured process:

1. **Prepare and Sample Datasets** to extract clean words.  
2. **Define a Correction Function** to match each distorted token with the closest clean word using RapidFuzz.  
3. **Use Parallel Processing** to speed up large-scale text correction.  
4. **Compute Token-Level Evaluation** metrics (precision, recall, F1).  

We assume you've already reviewed the dataset documentation [Dataset.md](https://github.com/SL6I/Text-Correction/blob/main/Dataset.md). Below is the detailed explanation and the complete code for this baseline.

---

## Overview of the Method

### 1. Sampling Clean Words
A small sample is taken from each dataset—1% from `dftrain` and 5% from both `dfdev` and `dftest`—to gather a set of unique **clean** words. This helps reduce computational load while retaining a representative vocabulary:

- **1%** of `dftrain` is sampled.  
- **5%** of `dfdev` and `dftest` are sampled.  
- All unique words from the `clean` column in these samples form our **reference** dictionary.

### 2. Distorted Data
Our datasets have columns with progressively “distorted” versions of the **clean** text. For instance, `distorted_0.05`, `distorted_0.10`, and `distorted_0.15` each introduce a different level of noise.

### 3. RapidFuzz Correction
For each token in the **distorted** text, we find the closest match in the reference dictionary using `process.extractOne(word, clean_words, scorer=fuzz.WRatio)`. If the match’s similarity score is above a threshold (e.g., `> 80`), we replace the distorted token with its best match.

As an Example:

<div align="center">
  <img src="https://github.com/user-attachments/assets/0910c12b-0f03-4291-9f8c-ae17755e366e" width="600" height="500" alt="Description of image">
</div>




### 4. Parallel Processing
To handle larger datasets efficiently, the correction function is applied in parallel using the Python `multiprocessing.Pool`.

### 5. Evaluation (Token-Level)
We evaluate using token-level **precision**, **recall**, and **F1-score**. We compare the **corrected** output tokens with the **clean** (ground-truth) tokens to measure how many were matched vs. how many were missed or wrongly added.

### Here Is The Result
![image](https://github.com/user-attachments/assets/f0c758f2-d6da-46d6-a181-8d78adb242e3)

