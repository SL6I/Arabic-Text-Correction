## Evaluation Function for Precision, Recall, and F1  
Precision, Recall, and F1 Score are commonly used metrics information retrieval to evaluate the performance of models, especially in classification tasks.  

# Precision
**Definition**: Precision measures the accuracy of a process by calculating the proportion of correct outcomes out of all the outcomes identified as positive. It evaluates how often the identified positives are actually correct.  
![image alt](https://github.com/SL6I/Text-Correction/blob/b9782b0223ecc585a681c05df0b78988d7dab499/Precision.png)    
**Purpose**:     
* Precision ensures that the system avoids unnecessary or incorrect changes to words or sentences.  
* High precision means that when the system corrects a word, it is likely to be correct.

# Recall  
**Definition**: Recall measures how many of the actual errors in the input text your system successfully corrected. It focuses on the system's ability to detect and fix errors.  
![image.png](https://github.com/SL6I/Text-Correction/blob/015b61f6e89d34e42fbf829873b08f6b31657a73/Recall.png)        
**Purpose**:     
* Recall ensures that the system does not miss necessary corrections.  
* High recall means the system is effective at finding and fixing errors.


# F1 Score  
**Definition**: The F1 Score is the harmonic mean of Precision and Recall. It provides a single metric that balances the trade-off between Precision and Recall, offering a comprehensive measure of performance.  
![image.png](https://github.com/SL6I/Text-Correction/blob/654b4a3c0b54540b6912d513f162b77d658187af/F1%20Score.png)    
**Purpose**:   
* F1 Score is useful when you need to balance the importance of both Precision and Recall.  
* In Arabic text correction, if the system is too conservative (high Precision, low Recall) or too aggressive (low Precision, high Recall), the F1 Score will drop.  
