# AraT5v2 With POS: Enhancing Arabic Text Correction with POS Tagging

This repository provides scripts for **fine-tuning** [AraT5v2-base-1024](https://huggingface.co/) with **Part-of-Speech (POS) tagging**, leveraging [Stanza](https://stanfordnlp.github.io/stanza/) for improved accuracy in Arabic text correction. By integrating syntactic and grammatical features, this extension significantly enhances correction performance and language understanding.

---

## Table of Contents
1. [Introduction](#introduction)
2. [What is POS Tagging?](#what-is-pos-tagging)
3. [Requirements](#requirements)
4. [Data Format](#data-format)
5. [Usage](#usage)
6. [Training](#training)
7. [Inference](#inference)
8. [Evaluation](#evaluation)
9. [Results](#results)

---

## Introduction

AraT5v2_with_pos improves grammatical error correction in Arabic by incorporating **POS tagging** into the model’s input pipeline. Enriching the linguistic context and enhancing correction performance. This model fine-tunes **AraT5v2-base-1024** using **POS-augmented data**.

### What is POS Tagging?

Part-of-Speech (POS) tagging is a process in Natural Language Processing (NLP) where each word in a sentence is assigned a grammatical category, such as noun, verb, or adjective. This helps in understanding the syntactic structure and improving various language tasks like text correction, machine translation, and sentiment analysis.
![image](https://github.com/user-attachments/assets/74aa300c-42af-49e8-89e0-3b078660ebda)

---

## Requirements

1. **Python 3.x**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Minimal dependencies:
   - `transformers`
   - `datasets`
   - `sentencepiece`
   - `stanza`
   - `tqdm`
3. **GPU (recommended)** for faster training.
4. **Creating the data using `data_with_pos_creating`**
5. **Navigate to the directory**:
   ```bash
   cd Extension/AraT5v2_with_pos
   ```

---

## Data Format

Each JSON file (train/dev/test) follows this format:
```json
{
  "prompt": "<task>تصحيح النص</task>\n<input>أنا لكتاب الكتاب</input>\n<pos_tags>أنا/PRON لكتاب/NOUN الكتاب/NOUN</pos_tags>\nالرجاء التصحيح.",
  "cor": "أنا كاتب الكتاب"
}
```
- **raw**: Uncorrected Arabic sentence with POS.
- **cor**: Corrected sentence.

---

## Usage

### Training

Run `finetune_arat5v2_pos.py`:
```bash
python finetune_arat5v2_pos.py \
  --train_file "../../Dataset/finetuning/AraT5v2+pos/train_processed_pos.json" \
  --dev_file "../../Dataset/finetuning/AraT5v2+pos/dev_processed_pos.json" \
  --output_dir "arat5v2_pos_checkpoints" \
  --epochs 5 \
  --learning_rate 1e-4
```

**Parameters**:
- `--train_file`: Path to training set.
- `--dev_file`: Path to dev set.
- `--output_dir`: Directory for checkpoints.
- `--epochs`: Training epochs (default 5).
- `--learning_rate`: Default `1e-4`.

---

### Inference

Run `predict_arat5v2_pos.py`:
```bash
python predict_arat5v2_pos.py \
  --model_dir "arat5v2_pos_checkpoints/saved_model" \
  --dev_file "../../Dataset/finetuning/AraT5v2+pos/dev_processed_pos.json" \
  --test_file "../../Dataset/finetuning/AraT5v2+pos/test_processed_pos.json" \
  --output_dir "predictions" \
  --max_length 1024 \
  --num_beams 5
```

**Parameters**:
- `--model_dir`: Path to fine-tuned model.
- `--dev_file`: Path to dev set.
- `--test_file`: Path to test set.
- `--output_dir`: Stores predictions.
- `--num_beams`: Beam search parameter.

---

## Evaluation

Using `m2scorer`:
```bash
python ../../Evaluation/Scripts/m2scorer.py \
  predictions/test_predictions.txt \
  ../../Dataset/Test/QALB-2014-L1-Test.m2
```

---

## Results

![image](https://github.com/user-attachments/assets/5eff2d26-0791-431f-a951-cf1179df63ee)


By incorporating POS tagging, **AraT5v2_with_pos** achieves **higher accuracy** and **better linguistic structure** in Arabic text correction.

---

**Happy Fine-Tuning!**

