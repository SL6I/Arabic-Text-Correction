#!/usr/bin/env python3
# build_baseline.py

import sys
import json
from collections import defaultdict, Counter

def build_majority_map(m2_file):
    """
    Parse the .m2 file, gather (incorrect_token -> list_of_corrections),
    then pick the single most frequent correction for each.
    Return a dict: majority_map[incorrect_token] = best_correction
    """
    freq_map = defaultdict(Counter)

    with open(m2_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Very simplified example:
    # We assume lines that start with "A " contain corrections.
    # This may need adaptation to QALB's actual format!
    current_source = None
    for line in lines:
        line = line.strip()
        if line.startswith("S "):
            # This is the source line
            current_source = line[2:].split()  # tokenized
        elif line.startswith("A "):
            # e.g. "A 3 4|||Edit|||somecorrection|||REQUIRED|||-NONE-|||0"
            fields = line[2:].split("|||")
            start_end = fields[0].strip().split()
            start_off, end_off = int(start_end[0]), int(start_end[1])
            # The corrected text(s)
            corrections_str = fields[2].strip()  # e.g. "somecorrection"
            corrections = corrections_str.split("||")  # if multiple

            # The original substring
            if current_source:
                # slice [start_off:end_off] from the current_source tokens
                original_tokens = current_source[start_off:end_off]
                original_str = " ".join(original_tokens)
            else:
                # fallback if you don't have the source tokens
                original_str = "???"

            for corr in corrections:
                corr = corr.strip()
                # We skip if it's "-NONE-" or empty
                if corr and corr != "-NONE-":
                    freq_map[original_str].update([corr])

    # Build the majority map
    majority_map = {}
    for orig_token, counter in freq_map.items():
        # pick the single highest count
        best_correction, _ = counter.most_common(1)[0]
        majority_map[orig_token] = best_correction

    return majority_map

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_baseline.py QALB-2014-L1-Train.m2")
        sys.exit(1)
    
    m2_file = sys.argv[1]
    majority_map = build_majority_map(m2_file)

    # Save to a file, e.g. JSON
    with open("majority_map.json", "w", encoding="utf-8") as f:
        json.dump(majority_map, f, ensure_ascii=False, indent=2)
    
    print(f"Saved majority_map.json with {len(majority_map)} entries.")

if __name__ == "__main__":
    main()
