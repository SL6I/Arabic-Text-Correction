## Evaluation Function for Precision, Recall, and F1
---
Precision, Recall, and F1 Score are commonly used metrics for information retrieval to evaluate the performance of models, especially in classification tasks.  

![image alt](https://github.com/SL6I/Text-Correction/blob/991296c33dfb164cabe364793939d8bd1000d632/Images/Metrics.png)  

- **True Positive (TP):** The system made a correction, and it was correct (fixed an actual error).    
- **False Positive (FP):** The system made a correction, but it was unnecessary or wrong.    
- **False Negative (FN):** There was an error in the text, but the system failed to correct it.    
- **True Negative (TN):** The system correctly left an already correct word unchanged.

---
# Precision  
**Definition:** Precision measures the accuracy of a process by calculating the proportion of correct outcomes out of all the outcomes identified as positive. It evaluates how often the identified positives are actually correct.  

![image alt](https://github.com/SL6I/Text-Correction/blob/0a5d1edf94f47136bd8fd17ca9b4d4f5c03e6284/Images/Precision.png)  

**Purpose:**     
* Precision ensures that the system avoids unnecessary or incorrect changes to words or sentences.  
* High precision means that when the system corrects a word, it is likely to be correct.
---

# Recall  
**Definition:** Recall measures how many of the actual errors in the input text the system successfully corrected. It focuses on the system's ability to detect and fix errors.  
![image.png](https://github.com/SL6I/Text-Correction/blob/0a5d1edf94f47136bd8fd17ca9b4d4f5c03e6284/Images/Recall.png)          
**Purpose:**     
* Recall ensures that the system does not miss necessary corrections.  
* High recall means the system is effective at finding and fixing errors.
---  

# F1 Score  
**Definition:** The F1 Score is the harmonic mean of Precision and Recall. It provides a single metric that balances the trade-off between Precision and Recall, offering a comprehensive measure of performance.  
![image.png](https://github.com/SL6I/Text-Correction/blob/991296c33dfb164cabe364793939d8bd1000d632/Images/F1%20Score.png)    
**Purpose:**   
* F1 Score is useful when you need to balance the importance of both Precision and Recall.  
* In Arabic text correction, if the system is too conservative (high Precision, low Recall) or too aggressive (low Precision, high Recall), the F1 Score will drop.  
---

# How to run the script
**Running the ```m2scorer``` Script:**
```bash
cd Evaluation/scripts
```

To score the dataset using the m2scorer.py script, use the following general form in the terminal:
``` bash
python m2scorer.py <input_corpus_file_path> <input_m2_file_path>
```

**Parameters:**

- ```<input_corpus_file_path>```: The path to the corpus file containing the original sentences (You may say the prediction of the model).
- ```<input_m2_file_path>```: The path to the M2 file containing the corrections.

**Example:**
``` bash
python m2scorer.py ../../Dataset/Test/QALB-2014-L1-Test.sent ../../Dataset/Test/QALB-2014-L1-Test.m2
```

> [!IMPORTANT]
> Python is already installed on your system.  
> Make sure you are in the `scripts` folder.  
> The m2scorer.py script and input files are available in the specified paths.  
--- 
# References:  
- (https://en.wikipedia.org/wiki/Precision_and_recall)
