# updating AraT5 to a new version for fine-tuning Arabic GEC tasks involves using customized scripts for training and predictions.
# AraT5v2: Fine-Tuning for Arabic GEC
Working through scripts for Arab T5 version 2 to tackle Arabic Grammatical Error Correction. Training involves using `finetune_arat5v2.py`, while predictions are handled with `predict_arat5v2.py`.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Data Format](#data-format)
4. [Usage](#usage)
5. [Train](#training)
6. [Prediction](#prediction)
7. [Evaluation](#evaluation)
8. [Result](#result)

---

## Introduction

More advanced model for Arabic Grammatical Error Correction, highlighting its updates and the dataset it uses.

---

## Requirements

1. **Python 3.x**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Minimal packages:
   - `transformers`
   - `datasets`
   - `sentencepiece`
   - `tqdm`
3. **GPU (recommended)** for faster training.
- **Navigate to the directory**: Move into the directory containing the files:
  ```bash
  cd Baseline/AraT5v2
   ```
---

## Data Format

Each JSON file (train/dev/test) follows:
```json
[
  { "raw": "أنا لكتاب الكتاب", "cor": "أنا كاتب الكتاب" },
  { "raw": "هذه بعض الكلمات الخاطأة", "cor": "هذه بعض الكلمات الخاطئة" }
]
```
- **raw**: Uncorrected Arabic sentence.
- **cor**: Corrected sentence.

---
# Usage
In the following code we will guide you how to run the code:
## Training

Run `finetune_arat5v2.py`:
```bash
python finetune_arat5v2.py `
  --train_file "train.json" `
  --dev_file "dev.json" `
  --output_dir "arat5v2_gec_checkpoints" `
  --epochs 5 `
  --learning_rate 1e-4
```

**Parameters**:
- `--train_file`: Path to training set.
- `--dev_file`: Path to dev set.
- `--output_dir`: Directory for checkpoints.
- `--epochs`: Training epochs (default 5).
- `--learning_rate`: Default `1e-4`.

---

## Inference

Run `predict_arat5v2.py`:
```bash
python predict_arat5v2.py \
  --model_dir "arat5v2_gec_checkpoints\saved_model" \
  --dev_file "dev.json" \
  --test_file "test.json" \
  --output_dir "predictions" \
  --max_length 1024 \
  --num_beams 5
```

**Parameters**:
- `--model_dir`: Folder of our fine-tuned model.
- `--dev_file`: Path to dev set.
- `--test_file`: Path to test set.
- `--output_dir`: Stores predictions.
- `--num_beams`: Beam parameter.

---

## Evaluation

Using `m2scorer`:
```bash
python ../../Evaluation/Scripts/m2scorer.py \
  predictions/test_predictions.txt \
  ../../Dataset/Test/QALB-2014-L1-Test.m2
```

---

## Result:


**Happy Fine-Tuning!**

