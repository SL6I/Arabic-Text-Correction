# Baseline for Arabic GEC

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
   cd scripts/Baseline
   ```
2. **Run**:
```bash
python rewriter.py `
  --train_file "scripts\Baseline\Sample\qalb14_train.areta.nopnx.txt" `
  --test_file "scripts\Baseline\Sample\qalb14_dev.areta.txt" `
  --mode full `
  --cbr_ngrams 2 `
  --output_path "scripts\Baseline\Sample"m,
```
