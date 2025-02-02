#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import random
import numpy as np
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
)
from datasets import load_dataset

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

def preprocess_function(examples, tokenizer, max_seq_length=1024):
    # Use the POS-enhanced "prompt" field instead of "raw"
    inputs = examples["prompt"]
    targets = examples["cor"]

    # Tokenize inputs with fixed padding and truncation
    model_inputs = tokenizer(
        inputs,
        max_length=max_seq_length,
        truncation=True,
        padding="max_length"
    )

    # Tokenize targets (labels)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            targets,
            max_length=max_seq_length,
            truncation=True,
            padding="max_length"
        )
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

def train_and_finetune(train_file, dev_file, output_dir, epochs=5, learning_rate=1e-4):
    # Set random seed for reproducibility
    set_seed(42)

    # Use the AraT5v2-base-1024 model
    model_name = "UBC-NLP/AraT5v2-base-1024"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Load datasets (each JSON file should have one JSON object per line)
    train_data = load_dataset("json", data_files=train_file, split="train")
    dev_data   = load_dataset("json", data_files=dev_file, split="train")

    # Preprocess the datasets
    train_dataset = train_data.map(
        lambda x: preprocess_function(x, tokenizer),
        batched=True,
        remove_columns=train_data.column_names
    )
    dev_dataset = dev_data.map(
        lambda x: preprocess_function(x, tokenizer),
        batched=True,
        remove_columns=dev_data.column_names
    )

    # Define training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        num_train_epochs=epochs,
        learning_rate=learning_rate,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        gradient_accumulation_steps=8,
        seed=42,
        logging_steps=100,
        load_best_model_at_end=True,
        metric_for_best_model="loss",
        greater_is_better=False,
        report_to="none"
    )

    # Data collator for Seq2Seq tasks
    data_collator = DataCollatorForSeq2Seq(
        tokenizer=tokenizer,
        model=model,
        padding="longest",
        return_tensors="pt"
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=dev_dataset,
        data_collator=data_collator,
    )

    # Start training
    trainer.train()

    # Save the model and tokenizer
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Model and tokenizer saved to: {output_dir}")

def main():
    parser = argparse.ArgumentParser(
        description="Fine-tune AraT5v2 model with POS-tagged data for text correction."
    )
    parser.add_argument("--train_file", type=str, required=True,
                        help="Path to the training JSON file with POS tags.")
    parser.add_argument("--dev_file", type=str, required=True,
                        help="Path to the development JSON file with POS tags.")
    parser.add_argument("--output_dir", type=str, default="araT5_gec_checkpoints_pos",
                        help="Directory where the fine-tuned model will be saved.")
    parser.add_argument("--epochs", type=int, default=5,
                        help="Number of training epochs.")
    parser.add_argument("--learning_rate", type=float, default=1e-4,
                        help="Learning rate for training.")

    args = parser.parse_args()

    train_and_finetune(
        train_file=args.train_file,
        dev_file=args.dev_file,
        output_dir=args.output_dir,
        epochs=args.epochs,
        learning_rate=args.learning_rate
    )

if __name__ == "__main__":
    main()
