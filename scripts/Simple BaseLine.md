# Sample Approach to Text Correction Using Majority-Class
### Introduction
This document outlines a **dictionary-based** baseline for text correction.

---
### 1) Build a Dictionary (Train Phase)

- **Goal**: Collect frequent replacements (from an `.m2` file).  
- **Method**: For each token that is changed in the gold reference, count how often it’s replaced by each correction.  
- **Output**: A dictionary from “incorrect token” → “most frequent correction”.

**Example**:
```bash
python build_baseline.py path/to/train.m2
```
- Produces a file `majority_map.json`, containing mappings like:
  ```json
  {
    "خطاء": "خطأ",
    "برامج": "برنامج",
    ...
  }
  ```

  ---
### 2) Apply the Dictionary (Inference Phase on the Test set)

- **Goal**: Correct new text using the dictionary.  
- **Method**: For each token in each sentence:
  1. If it’s in `majority_map` replace it with the known “most frequent correction”  
  2. Otherwise, leave it alone.  
- **Output**: A file `baseline_output.txt` with corrected sentences of the bad one.

**Example**:
```bash
python simple_baseline.py majority_map.json path/to/dev.sent
```
- Will Produce `baseline_output.txt`.

---

### 3) Evaluate (Precision, Recall, F-score)

- **Goal**: Compare your baseline’s corrected output with a gold reference (`.m2`) file.  
- **Method**: Use `m2scorer.py`, which reports how many edits were correct vs missed.

**Example**:
```bash
python m2scorer.py baseline_output.txt path/to/dev.m2
```
- Outputs lines like (it's actually worse):
  ```
  Precision   : 0.55
  Recall      : 0.55
  F_0.5       : 0.55
  ```

  ---
## Files and Steps Recap

1. **`build_baseline.py`**:  
   - Input: Training `.m2` file (contains wrong sentences with its edit for each token).
   - Output: `majority_map.json` (dictionary).

2. **`simple_baseline.py`**:  
   - Input: `majority_map.json` + original sentences (`test.sent`) > contains the errors.
   - Output: `baseline_output.txt` (the corrected version)

3. **`m2scorer.py`**:  
   - Compares `baseline_output.txt` to a gold `.m2`  
   - Prints precision, recall, F-score  

### The Result
![image](https://github.com/SL6I/Text-Correction/blob/ed62f6148f8c9e030ab284cb05eccd6228144db9/Images/Simple%20Baseline.jpg)
