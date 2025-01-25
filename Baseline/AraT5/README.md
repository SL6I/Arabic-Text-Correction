# AraT5: Fine-Tuning for Arabic GEC

This repository provides scripts for **fine-tuning** [UBC-NLP/araT5-base](https://huggingface.co/UBC-NLP/araT5-base) on Arabic Grammatical Error Correction tasks. You can train the model using `finetune_arat5.py` and generate predictions with `predict_arat5.py`.

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

Arabic Grammatical Error Correction (GEC) detects and corrects grammatical mistakes in Arabic text. This repository fine-tunes **AraT5**, a variant of the T5 model, on Qalb-2014.

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
  cd Baseline/AraT5
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

Run `finetune_arat5.py`:
```bash
python finetune_arat5.py \
  --train_file "train.json" \
  --dev_file "dev.json" \
  --output_dir "arat5_gec_checkpoints" \
  --epochs 15 \
  --learning_rate 1e-4
```

**Parameters**:
- `--train_file`: Path to training set.
- `--dev_file`: Path to dev set.
- `--output_dir`: Directory for checkpoints.
- `--epochs`: Training epochs (default 15).
- `--learning_rate`: Default `1e-4`.

---

## Inference

Run `predict_arat5.py`:
```bash
python predict_arat5.py \
  --model_dir "arat5_gec_checkpoints\saved_model" \
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
  test.json
```

---

## Result:

**Happy Fine-Tuning!**
