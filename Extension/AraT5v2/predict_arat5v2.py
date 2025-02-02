#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser(
        description="Run inference with a fine-tuned AraT5v2 model."
    )
    parser.add_argument(
        "--model_dir", type=str, required=True,
        help="Path to the fine-tuned model directory (checkpoint)."
    )
    parser.add_argument(
        "--dev_file", type=str, required=False,
        help="Path to the development JSON file. If not provided, dev predictions are skipped."
    )
    parser.add_argument(
        "--test_file", type=str, required=False,
        help="Path to the test JSON file. If not provided, test predictions are skipped."
    )
    parser.add_argument(
        "--output_dir", type=str, default="predictions",
        help="Directory to save prediction outputs."
    )
    parser.add_argument(
        "--max_length", type=int, default=1024,
        help="Maximum generation length."
    )
    parser.add_argument(
        "--num_beams", type=int, default=5,
        help="Number of beams for beam search."
    )

    args = parser.parse_args()

    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load tokenizer and model from the fine-tuned checkpoint directory
    tokenizer = AutoTokenizer.from_pretrained(args.model_dir, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(args.model_dir)
    model.to(device)

    # Ensure the output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    def predict(dataset, name):
        preds = []
        for sample in tqdm(dataset, desc=f"Predicting on {name} data"):
            input_text = sample["raw"]
            # Tokenize input text
            tokenized_inp = tokenizer.encode(input_text, return_tensors="pt").to(device)

            # Generate output using beam search
            outputs = model.generate(
                tokenized_inp,
                max_length=args.max_length,
                num_beams=args.num_beams
            )
            pred_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            preds.append(pred_text)

        out_file = os.path.join(args.output_dir, f"{name}_predictions.txt")
        with open(out_file, "w", encoding="utf-8") as f:
            for pred in preds:
                f.write(pred.strip() + "\n")
        print(f"{name.capitalize()} predictions saved to {out_file}")

    # Run predictions on the dev set if provided
    if args.dev_file:
        dev_data = load_dataset("json", data_files=args.dev_file, split="train")
        predict(dev_data, "dev")

    # Run predictions on the test set if provided
    if args.test_file:
        test_data = load_dataset("json", data_files=args.test_file, split="train")
        predict(test_data, "test")


if __name__ == "__main__":
    main()
