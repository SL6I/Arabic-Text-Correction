Introduction
This document outlines a straightforward dictionary-based baseline for text correction. By collecting token-level mappings from raw (erroneous) tokens to their most common corrections, we can automatically fix errors in unseen text. The following sections describe how we build the dictionary, apply it to new sentences, and evaluate the results using precision, recall, and F1-score.
