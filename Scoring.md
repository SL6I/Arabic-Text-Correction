## Evaluation Function for Precision, Recall, and F1  
Precision, Recall, and F1 Score are commonly used metrics information retrieval to evaluate the performance of models, especially in classification tasks.  
![image alt](https://github.com/SL6I/Text-Correction/blob/bc8ecdf859ecc6285ca2bfd7c8d56a256208272d/Metrics.png)  
- **True Positive (TP):** The system made a correction, and it was correct (fixed an actual error).  
- **False Positive (FP):** The system made a correction, but it was unnecessary or wrong.  
- **False Negative (FN):** There was an error in the text, but the system failed to correct it.  
- **True Negative (TN):** The system correctly left an already correct word unchanged.  
# Precision
**Definition:** Precision measures the accuracy of a process by calculating the proportion of correct outcomes out of all the outcomes identified as positive. It evaluates how often the identified positives are actually correct.  
![image alt](https://github.com/SL6I/Text-Correction/blob/b9782b0223ecc585a681c05df0b78988d7dab499/Precision.png)    
**Purpose:**     
* Precision ensures that the system avoids unnecessary or incorrect changes to words or sentences.  
* High precision means that when the system corrects a word, it is likely to be correct.

# Recall  
**Definition:** Recall measures how many of the actual errors in the input text the system successfully corrected. It focuses on the system's ability to detect and fix errors.  
![image.png](https://github.com/SL6I/Text-Correction/blob/015b61f6e89d34e42fbf829873b08f6b31657a73/Recall.png)        
**Purpose:**     
* Recall ensures that the system does not miss necessary corrections.  
* High recall means the system is effective at finding and fixing errors.


# F1 Score  
**Definition:** The F1 Score is the harmonic mean of Precision and Recall. It provides a single metric that balances the trade-off between Precision and Recall, offering a comprehensive measure of performance.  
![image.png](https://github.com/SL6I/Text-Correction/blob/654b4a3c0b54540b6912d513f162b77d658187af/F1%20Score.png)    
**Purpose:**   
* F1 Score is useful when you need to balance the importance of both Precision and Recall.  
* In Arabic text correction, if the system is too conservative (high Precision, low Recall) or too aggressive (low Precision, high Recall), the F1 Score will drop.  


# How to run score.py
To run score.py, you must provide three input files that serve different purposes. Each file represents a different stage of the text correction process. Below, I'll guide you on how to properly prepare the required files and how to modify score.py to accept and handle these files correctly.  
The Three Input Files:  
- gold_file: This file contains the correct text, which serves as the reference or "ground truth". It should have no errors.  
- raw_file: This file contains the original text, which may contain errors or issues (e.g., spelling mistakes, grammar issues, etc.).
- pred_file: This file contains the predicted or corrected text. It should be the output of your model or manual corrections applied to the raw_file.

# References  
- https://aclanthology.org/2023.emnlp-main.396.pdf  
