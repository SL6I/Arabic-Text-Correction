# Simple Baseline for Arabic GEC

**MLE-based rewriting approach** for Arabic Grammatical Error Correction. It learns probabilities of `(source_token → target_token)` conditioned on GED tags **(optional)** or gold tags.

## Overview
1. **Train** a CBR (Corpus-Based Rewriting) model from a `train_file` containing `(src, tgt, tag)`.
2. **Rewrite** a `test_file` by substituting each token according to the learned probabilities.
3. **If no GED model** is specified, the system uses **gold tags** from the test data.

## Usage

```bash
python rewriter.py \
  --train_file scripts/BaseLine/Sample/qalb14_train.areta.nopnx.txt \
  --test_file scripts/BaseLine/Sample/qalb14_dev.areta.txt \
  --mode full \
  --cbr_ngrams 2 \
  --output_path scripts/BaseLine/Sample \
  [--ged_model path/to/ged_model] \
  [--do_error_ana]
