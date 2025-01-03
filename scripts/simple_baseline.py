#!/usr/bin/env python3
# simple_baseline.py

import sys
import json

def apply_majority_baseline(input_sents, majority_map):
    corrected_sents = []
    for line in input_sents:
        tokens = line.split()
        new_tokens = []
        for t in tokens:
            if t in majority_map:
                new_tokens.append(majority_map[t])
            else:
                new_tokens.append(t)
        corrected_sents.append(" ".join(new_tokens))
    return corrected_sents

def main():
    if len(sys.argv) < 3:
        print("Usage: python simple_baseline.py majority_map.json input_sentences.txt")
        sys.exit(1)

    map_file = sys.argv[1]
    input_file = sys.argv[2]

    # 1) Load the majority_map
    with open(map_file, "r", encoding="utf-8") as f:
        majority_map = json.load(f)

    # 2) Load the input sentences (dev/test)
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f]

    # 3) Apply baseline
    corrected = apply_majority_baseline(lines, majority_map)

    # 4) Write to file
    output_file = "baseline_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for c in corrected:
            f.write(c + "\n")

    print(f"Baseline output written to {output_file}.")

if __name__ == "__main__":
    main()
