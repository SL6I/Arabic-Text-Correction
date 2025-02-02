#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from tqdm import tqdm
import stanza

# If you run this for the first time, uncomment the following lines:
# pip install stanza
# stanza.download('ar')

# Initialize Stanza's Arabic pipeline with tokenization and POS tagging
nlp = stanza.Pipeline('ar', processors='tokenize,pos', tokenize_pretokenized=False)

# Define the input directory where your original JSON files (train.json, dev.json, test.json) are located.
# You can modify this path as needed.
INPUT_DIR = os.path.join("Dataset", "finetuning", "AraT5-AraT5v2")

# Define the output directory where processed files with POS tags will be saved.
OUTPUT_DIR = os.path.join("Dataset", "finetuning", "AraT5v2+pos")

def pos_tag_sentence(sentence):
    """
    Performs POS tagging on a given Arabic sentence using Stanza.
    Returns a list of tuples: (word, POS tag)
    """
    doc = nlp(sentence)
    pos_tags = []
    for sent in doc.sentences:
        for word in sent.words:
            pos_tags.append((word.text, word.upos))  # Using Universal POS tags
    return pos_tags  # List of (word, POS) tuples

def format_pos_tags(pos_tags):
    """
    Formats POS tags into a string for inclusion in the prompt.
    Example: "word1/POS1 word2/POS2 ..."
    """
    return ' '.join([f"{word}/{tag}" for word, tag in pos_tags])

def process_json_file_in_batch(json_in, json_out):
    """
    1) Read JSON lines from json_in using tqdm.
    2) Perform POS tagging on "raw" texts.
    3) Write final JSON lines to json_out with a tagged "prompt".
    """

    # 1) Read JSON lines
    data_list = []
    with open(json_in, "r", encoding="utf-8") as fin:
        print(f"\nReading JSON from {os.path.basename(json_in)}...")
        for line in tqdm(fin, desc="Reading JSON lines"):
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            data_list.append(obj)

    print(f"Loaded {len(data_list)} lines from {json_in}.")

    # 2) Perform POS tagging on 'raw' texts
    print("\nPerforming POS tagging on 'raw' texts...")
    pos_tags_list = []
    for obj in tqdm(data_list, desc="POS Tagging"):
        raw_text = obj.get("raw", "")
        pos_tags = pos_tag_sentence(raw_text)
        formatted_pos = format_pos_tags(pos_tags)
        pos_tags_list.append(formatted_pos)

    # 3) Merge POS tags with the original data and write output
    print(f"\nMerging POS tags with original data and writing to {json_out}...")
    with open(json_out, "w", encoding="utf-8") as fout:
        for obj, pos_tags in tqdm(zip(data_list, pos_tags_list), total=len(data_list), desc="Merging & Writing"):
            raw_text = obj.get("raw", "")
            cor_text = obj.get("cor", "")

            # Construct the tagged prompt
            prompt = (
                "<task>تصحيح النص</task>\n"
                f"<input>{raw_text.strip()}</input>\n"
                f"<pos_tags>{pos_tags}</pos_tags>\n"
                "الرجاء التصحيح."
            )

            new_obj = {
                "prompt": prompt,
                "cor": cor_text  # The corrected text
            }
            fout.write(json.dumps(new_obj, ensure_ascii=False) + "\n")

    print(f"✅ Done processing {json_in} → {json_out}.")

def main():
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # List of files to process
    files = ["train.json", "dev.json", "test.json"]
    for fname in files:
        json_in = os.path.join(INPUT_DIR, fname)
        if os.path.exists(json_in):
            json_out = os.path.join(OUTPUT_DIR, fname.replace(".json", "_processed_pos.json"))
            process_json_file_in_batch(json_in, json_out)
        else:
            print(f"File not found: {json_in}")

if __name__ == "__main__":
    main()
