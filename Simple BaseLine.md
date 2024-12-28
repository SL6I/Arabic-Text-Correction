# Simple-Baseline: Sample Approach to Text Correction

### Introduction
This document outlines a simple dictionary-based baseline for text correction. We can automatically fix errors in unseen text by collecting token-level mappings from raw (erroneous) tokens to their most common corrections. The following sections describe how we build the dictionary, apply it to new sentences, and evaluate the results using precision, recall, and F1-score.  

---
## Overview of the Method
---
### 1. Build a Token-Level Dictionary
- We read pairs of parallel files: one with raw/erroneous sentences and one with their corrected counterparts.
- Each token in the raw text is aligned with the corresponding token in the corrected text.
- For any token that differs from its corrected version, we count how many times that correction occurs.
---
### 2. Apply the Dictionary to New Text
- We split a new (possibly erroneous) sentence into tokens.
- For each token, we look up its best-known correction in the dictionary.
- If the token is found in the dictionary, we replace it. Otherwise, we leave it as is.
---
### 3. Evaluation (Precision, Recall, F1)
- We use a function that compares raw tokens, their corrected and our predicted corrections.
- We accumulate counts of true positives (TP), false positives (FP), and false negatives (FN).
- From these counts, we compute precision, recall, and F1-score as standard measures of correction quality.
---
### The Result
![image](https://github.com/SL6I/Text-Correction/blob/6573d07542c5943edbb5c7cfff10d0b262fd9781/Images/Simple%20Baseline.png)
