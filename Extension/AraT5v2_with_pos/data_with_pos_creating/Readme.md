# Data POS Tagging Script

This script processes Arabic JSON files by performing POS tagging on the `"raw"` texts using Stanza and creating a tagged prompt for grammatical error correction.

## Requirements

- Python 3.x
- [Stanza](https://stanfordnlp.github.io/stanza/)
- tqdm

Install the dependencies with:
```bash
pip install stanza tqdm
```
*If running for the first time, uncomment the `stanza.download('ar')` line in the script to download the Arabic model.*

## Data Format

Each input JSON file should have lines like:
```json
{"raw": "أنا لكتاب الكتاب", "cor": "أنا كاتب الكتاب"}
```

Each output JSON file should have lines like:
```json
{
  "prompt": "<task>تصحيح النص</task>\n<input>أنا لكتاب الكتاب</input>\n<pos_tags>أنا/PRON لكتاب/NOUN الكتاب/NOUN</pos_tags>\nالرجاء التصحيح.",
  "cor": "أنا كاتب الكتاب"
}
```
## Usage

1. **Input Files:**  
   Place your input files (`train.json`, `dev.json`, `test.json`) in:
   ```
   Dataset/finetuning/AraT5-AraT5v2
   ```

2. **Output:**  
   Processed files with POS tags will be saved in:
   ```
   Dataset/finetuning/AraT5v2+pos
   ```

3. **Run the Script:**  
   Execute the script from the project root:
   ```bash
   python Extension/AraT5v2_with_pos/data_with_pos_creating/data_pos.py
   ```

Happy POS tagging!

