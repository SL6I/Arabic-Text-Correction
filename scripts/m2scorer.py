#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of the NUS M2 scorer.
# The NUS M2 scorer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The NUS M2 scorer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# file: m2scorer.py
#
# Usage (example):
#   python m2scorer.py [OPTIONS] system_output.txt gold.m2
#
# Options:
#   -v  --verbose
#   --very_verbose
#   --max_unchanged_words N
#   --beta B
#   --ignore_whitespace_casing
#
# You NEED a working `levenshtein.py` with:
#    batch_multi_pre_rec_f1(system_sents, source_sents, gold_edits, max_unchanged_words, beta, ignore_ws, verbose, vv)
# that returns (precision, recall, fscore).


import sys
from getopt import getopt

# Import these from your local project or any folder you placed them:
import levenshtein
from util import paragraphs, smart_open
# import levenshtein


def load_annotation(gold_file, verbose=False):
    """
    Read the entire .m2 gold file and extract:
      1) source_sentences (list)
      2) gold_edits (list of dict-of-lists)

    The data structure gold_edits is a list of dicts. For each sentence i:
       gold_edits[i] = {
         0: [(start, end, original, corrections), ...],  # annotator 0
         1: [...],  # annotator 1
         ...
       }

    Because this code was originally for Python2, we adapt it for Python3.

    QALB M2 might differ from standard M2; adapt if needed.
    """
    source_sentences = []
    gold_edits = []

    # read entire file as unicode text
    with open(gold_file, 'r', encoding='utf-8') as fgold:
        puffer = fgold.read()

    # break file into paragraphs
    paragraph_list = paragraphs(puffer.splitlines(True))

    for item in paragraph_list:
        lines = item.splitlines(False)
        # find the S line(s)
        sentence_lines = [line[2:].strip() for line in lines if line.startswith('S ')]
        if not sentence_lines:
            continue  # skip if no S line
        annotations = {}

        # gather all A lines
        for line in lines:
            line = line.strip()
            if line.startswith('A '):
                # e.g. A 0 1|||Edit|||some correction|||REQUIRED|||-NONE-|||0
                fields = line[2:].split('|||')
                start_offset = int(fields[0].split()[0])
                end_offset   = int(fields[0].split()[1])
                etype        = fields[1].strip()
                # if it's 'noop', ignore
                if etype == 'noop':
                    start_offset = -1
                    end_offset   = -1
                corrections = [c.strip() if c != '-NONE-' else '' 
                               for c in fields[2].split('||')]
                # original text from the source (not strictly needed for scoring)
                # but we keep it for debug
                # we'll find it from the entire sentence:
                # which might be multiple lines in sentence_lines, so join them
                joined_sentence = " ".join(sentence_lines)
                original = ' '.join(joined_sentence.split()[start_offset:end_offset])
                annotator = int(fields[5])

                if annotator not in annotations:
                    annotations[annotator] = []
                annotations[annotator].append((start_offset, end_offset, original, corrections))

        # QALB sometimes has multiple S lines. We handle them cumulatively:
        tok_offset = 0
        for this_sentence in sentence_lines:
            token_count = len(this_sentence.split())
            tok_offset_end = tok_offset + token_count
            source_sentences.append(this_sentence)

            # Filter edits for this portion
            this_edits = {}
            for ann_id, edits in annotations.items():
                filtered = []
                for e in edits:
                    st, en, orig, corr = e
                    # keep if it falls within [tok_offset, tok_offset_end)
                    if st >= tok_offset and en <= tok_offset_end and st >= 0 and en >= 0:
                        # shift offsets so they are local to this sub-sentence
                        st2 = st - tok_offset
                        en2 = en - tok_offset
                        filtered.append((st2, en2, orig, corr))
                this_edits[ann_id] = filtered

            # if no edits
            if all(len(v) == 0 for v in this_edits.values()):
                this_edits[0] = []

            gold_edits.append(this_edits)
            tok_offset = tok_offset_end

    if verbose:
        print(f"[load_annotation] Found {len(source_sentences)} source sentences.", file=sys.stderr)
        total_edits = sum(sum(len(v) for v in d.values()) for d in gold_edits)
        print(f"[load_annotation] Found {total_edits} total gold edits.", file=sys.stderr)

    return source_sentences, gold_edits


def print_usage():
    """ Print usage instructions. """
    print("Usage: m2scorer.py [OPTIONS] proposed_sentences gold_source", file=sys.stderr)
    print("where", file=sys.stderr)
    print("  proposed_sentences   -   system output, sentence per line", file=sys.stderr)
    print("  source_gold          -   source sentences with gold token edits", file=sys.stderr)
    print("OPTIONS", file=sys.stderr)
    print("  -v    --verbose                   -  print verbose output", file=sys.stderr)
    print("        --very_verbose              -  print lots of verbose output", file=sys.stderr)
    print("        --max_unchanged_words N     -  Maximum unchanged words. Default 2.", file=sys.stderr)
    print("        --beta B                    -  Beta value for F-measure. Default 0.5.", file=sys.stderr)
    print("        --ignore_whitespace_casing  -  Ignore edits that only affect whitespace/case. Default no.", file=sys.stderr)


# Default parameters
max_unchanged_words = 2
beta                = 0.5
ignore_whitespace_casing = False
verbose            = False
very_verbose       = False

if __name__ == "__main__":
    # parse command-line
    opts, args = getopt(
        sys.argv[1:], 
        "v", 
        ["max_unchanged_words=", "beta=", "verbose", 
         "ignore_whitespace_casing", "very_verbose"]
    )

    for o, v in opts:
        if o in ('-v', '--verbose'):
            verbose = True
        elif o == '--very_verbose':
            very_verbose = True
        elif o == '--max_unchanged_words':
            max_unchanged_words = int(v)
        elif o == '--beta':
            beta = float(v)
        elif o == '--ignore_whitespace_casing':
            ignore_whitespace_casing = True
        else:
            print(f"Unknown option: {o}", file=sys.stderr)
            print_usage()
            sys.exit(1)

    if len(args) != 2:
        print_usage()
        sys.exit(1)

    system_file = args[0]
    gold_file   = args[1]

    # 1) Load the gold data
    source_sentences, gold_edits = load_annotation(gold_file, verbose=verbose)

    # 2) Load the system output
    system_sentences = []
    with open(system_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            system_sentences.append(line.strip())
    if verbose:
        print(f"[main] Loaded {len(system_sentences)} system sentences.", file=sys.stderr)

    # 3) Call the Levenshtein-based scoring function
    # Make sure your 'levenshtein.py' actually has an implementation
    # and doesn't just return (0.5, 0.5, 0.5).
    p, r, f1 = levenshtein.batch_multi_pre_rec_f1(
        system_sentences,
        source_sentences,
        gold_edits,
        max_unchanged_words,
        beta,
        ignore_whitespace_casing,
        verbose,
        very_verbose
    )

    # 4) Print scores
    print(f"Precision   : {p:.4f}")
    print(f"Recall      : {r:.4f}")
    print(f"F_{beta:.1f}       : {f1:.4f}")
#