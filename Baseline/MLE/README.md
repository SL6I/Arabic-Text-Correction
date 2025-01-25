# Baseline for Arabic Grammatical Error Correction (GEC) Using MLE

-  [MLE](#mle-bi-gram)
-  [Results](#result)


# MLE (Bi-gram):
An **MLE-based rewriting approach** for Arabic Grammatical Error Correction. It learns probabilities of `(source_token → target_token)` from a training file and applies them to a test file.

## Overview
1. **Train** a CBR (Corpus-Based Rewriting) model from `(src, tgt, tag)` data.
2. **Rewrite** a test file by substituting each token according to the learned probabilities.

## Example

### Input: 
- Input text provided by a user or system.
- The text " لكتاب " has a mistake.

```json
  {Input (Test File):" انا لكتاب الكتاب "}
  ```
### Training Data: 
- The training data shows the system how to fix mistakes by providing examples of incorrect words and their correct replacements.
- using a replacement operation of the incorrect word "لكتب" to the correct word "كتب".
```json
  {Training Data:" لكتاب -> كاتب | replace "}
  ```
### Correct Output: 
- This is expected output after applying the correction to the input.
- The system replaces "لكتب" with "كتب" to produce the corrected sentence.

```json
  {Correct Output:" أنا كاتب الكتاب "}
  ```
  


## Usage
1. **Clone** this repo and navigate to the baseline scripts:
   ```bash
   cd Baseline/MLE
   ```
2. **Run**:
```bash
python Scripts/rewriter.py `
  --train_file "Sample/qalb14_train.areta.nopnx.txt" `
  --test_file "Sample/qalb14_dev.areta.txt" `
  --mode full `
  --cbr_ngrams 2 `
  --output_path "Sample"
```


# Result
![Uploading image.png…]()

