# AraT5 for Arabic Grammatical Error Correction (GEC)

AraT5 is a transformer-based model fine-tuned for Arabic Grammatical Error Correction tasks. This guide provides step-by-step instructions to train, evaluate, and generate predictions using AraT5.

## Overview

1. **Train** the AraT5 model using training and development datasets.
2. **Predict** corrections for input texts using a fine-tuned AraT5 model.
3. **Evaluate** the model's performance on a test dataset.

---

## Prerequisites

### Python Environment
- **Python 3.x**: Ensure Python is installed on your system.
- **Dependencies**: Install the required Python libraries:
  ```bash
  pip install -r requirements.txt
    ```
- **Navigate to the directory**: Move into the directory containing the files:
  ```bash
  cd Baseline\AraT5
   ```
  ---
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
---

## How to Run
1. Fine-Tuning AraT5
Train the model using the finetune_arat5.py script:
```bash
python finetune_arat5.py \
  --train_file "train.json" \
  --dev_file "dev.json" \
  --output_dir "arat5_gec_checkpoints" \
  --epochs 15 \
  --learning_rate 1e-4
```

2. Generating Predictions
Generate predictions for the test dataset using the fine-tuned model:


```bash
python predict_arat5.py \
  --model_dir "arat5_gec_checkpoints\saved_model" \
  --dev_file "dev.json" \
  --test_file "test.json" \
  --output_dir "predictions" \
  --max_length 1024 \
  --num_beams 5
```

3. Evaluation
Evaluate the model's performance using the m2scorer.py script:
```bash
python ../../Evaluation/Scripts/m2scorer.py predictions/test_predictions.txt test.json
  ```
