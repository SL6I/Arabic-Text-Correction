#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
from datasets import load_dataset
import random
import numpy as np
from tqdm import tqdm
import os

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

def preprocess_function(examples, tokenizer, max_seq_length=1024):
    inputs = examples["raw"]
    targets = examples["cor"]
    
    # Tokenize the inputs
    model_inputs = tokenizer(
        inputs,
        max_length=max_seq_length,
        truncation=True
    )
    
    # Tokenize the targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            targets,
            max_length=max_seq_length,
            truncation=True
        )
        
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

def train_and_predict(train_file, dev_file, test_file, output_dir, epochs=15, learning_rate=1e-4):
    # Set random seeds for reproducibility
    set_seed(42)
    
    # Model & Tokenizer
    model_name = "UBC-NLP/araT5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    # Load datasets from local JSON files
    train_data = load_dataset("json", data_files=train_file, split="train")
    dev_data   = load_dataset("json", data_files=dev_file,   split="train")
    test_data  = load_dataset("json", data_files=test_file,  split="train")
    
    # Preprocess
    train_dataset = train_data.map(lambda x: preprocess_function(x, tokenizer), batched=True)
    dev_dataset   = dev_data.map(lambda x: preprocess_function(x, tokenizer), batched=True)
    # We do not strictly need to preprocess the test_data for generation (we'll do it on the fly), but let's keep it consistent:
    test_dataset  = test_data.map(lambda x: preprocess_function(x, tokenizer), batched=True)
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        num_train_epochs=epochs,
        learning_rate=learning_rate,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        gradient_accumulation_steps=8,
        seed=42,
        logging_steps=100,
        load_best_model_at_end=True,
        metric_for_best_model="loss",
        greater_is_better=False,
        report_to="none"
    )
    
    # Data collator
    data_collator = DataCollatorForSeq2Seq(
        tokenizer=tokenizer,
        model=model,
        padding="longest",
        return_tensors="pt"
    )
    
    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=dev_dataset,
        data_collator=data_collator,
    )
    
    # Train
    trainer.train()
    
    # Save Model & Tokenizer
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Model and tokenizer saved to: {output_dir}")
    
    # (Re)Load the trained model for inference
    tokenizer = AutoTokenizer.from_pretrained(output_dir, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(output_dir)
    
    # Move model to GPU if available if we can so that it run fast
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Predict on Dev set
    dev_predictions = []
    for sample in tqdm(dev_data, desc="Predicting on dev data"):
        input_text = sample["raw"]
        tokenized_inp = tokenizer.encode(input_text, return_tensors="pt").to(device)
        
        outputs = model.generate(
            tokenized_inp,
            max_length=1024,
            num_beams=5
        )
        pred_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        dev_predictions.append(pred_text)
    
    dev_pred_file = os.path.join(output_dir, "dev_predictions.txt")
    with open(dev_pred_file, "w", encoding="utf-8") as f:
        for pred in dev_predictions:
            f.write(pred.strip() + "\n")
    print(f"Dev predictions saved to {dev_pred_file}")

    # Predict on Test set
    test_predictions = []
    for sample in tqdm(test_data, desc="Predicting on test data"):
        input_text = sample["raw"]
        tokenized_inp = tokenizer.encode(input_text, return_tensors="pt").to(device)
        
        outputs = model.generate(
            tokenized_inp,
            max_length=1024,
            num_beams=5
        )
        pred_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        test_predictions.append(pred_text)
    
    test_pred_file = os.path.join(output_dir, "test_predictions.txt")
    with open(test_pred_file, "w", encoding="utf-8") as f:
        for pred in test_predictions:
            f.write(pred.strip() + "\n")
    print(f"Test predictions saved to {test_pred_file}")

def main():
    parser = argparse.ArgumentParser(description="Fine-tune AraT5 locally and run predictions.")
    parser.add_argument("--train_file", type=str, required=True, help="Path to the training JSON file.")
    parser.add_argument("--dev_file",   type=str, required=True, help="Path to the dev JSON file.")
    parser.add_argument("--test_file",  type=str, required=True, help="Path to the test JSON file.")
    parser.add_argument("--output_dir", type=str, default="arat5_gec_checkpoints", help="Where to save the fine-tuned model.")
    parser.add_argument("--epochs",     type=int, default=15,    help="Number of training epochs.")
    parser.add_argument("--learning_rate", type=float, default=1e-4, help="Learning rate for training.")
    
    args = parser.parse_args()

    train_and_predict(
        train_file=args.train_file,
        dev_file=args.dev_file,
        test_file=args.test_file,
        output_dir=args.output_dir,
        epochs=args.epochs,
        learning_rate=args.learning_rate
    )

if __name__ == "__main__":
    main()
