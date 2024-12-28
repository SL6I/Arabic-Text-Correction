## Overview  
---
The QALB-2014-L1 dataset, sourced from the QALB project, is designed to support research in Arabic grammatical error correction. It includes a rich collection of annotated texts, arranged into training, development, and testing sets to aid in the development and testing of machine learning models for Arabic natural language processing.

---

## Dataset Contents
---
* QALB-2014-L1-Train/Test/Dev`.column`: These files provide comprehensive annotations for Arabic words, highlighting their morphological features and grammatical properties, including parts of speech and lemmas.
      
* QALB-2014-L1-Train/Test/Dev`.cor`: These files contain the finalized, corrected versions of Arabic sentences, which serve as benchmarks for evaluating the performance of text correction technologies.
  
* QALB-2014-L1-Train/Test/Dev`.m2`: Error annotations and corrections in `.m2` format, used for training and testing grammatical error correction systems.
  
* QALB-2014-L1-Train/Test/Dev`.sent`: Includes Arabic sentences with potential grammatical errors for text correction tasks, with **19,411** sentences in Train, **1,017** in Dev, and **968** in Test.

- **Train:**    
  The **training set** is used to develop Arabic grammatical error correction models. It includes a substantial number of original sentences paired with corrections and error annotations, allowing models to learn common grammatical mistakes and their appropriate remedies.

- **Development (Dev):**    
  The **development set** is used to fine-tune model parameters and evaluate intermediate performance. It helps prevent overfitting and ensures good generalization to unseen data.

- **Test:**    
  The **test set** is used to evaluate the final performance of trained models, offering an unbiased assessment of how effectively they correct grammatical errors in new, unseen Arabic text.
---
## Sample Data
---
**S إلياهو فينوغراد يتنبأ بسيل من الهجمات الإيرانية واللني إما ستسقط فوق مناطق العرب وبعض البنايات الخاليه أو تصوير لبعض الجثث الحيه وهي تنقل فوق الطائرات وغيرها من فبركات هوليووديه إعلاميه . العداء الإيراني ليس إلا نموذج من الكذب الممنهج على طريقة النازي هتلر .**  
`A 7 8|||Edit|||والتي|||REQUIRED|||-NONE-|||0`  
`A 15 16|||Edit|||الخالية|||REQUIRED|||-NONE-|||0`  
`A 20 21|||Edit|||الحية|||REQUIRED|||-NONE-|||0`  
`A 28 29|||Edit|||هوليوودية|||REQUIRED|||-NONE-|||0`  
`A 29 30|||Edit|||إعلامية|||REQUIRED|||-NONE-|||0`  
`A 35 36|||Edit|||نموذجا|||REQUIRED|||-NONE-|||0`  

* A: Denotes an annotation.

* 7 8: Range of index in the text where the correction is applied. This correction changes the word at indexes 7 to 8.

* Edit: Type of annotation, indicating a modification of existing content.  

* <span dir="ltr">**والتي**: Corrected content to replace the original.</span>

* REQUIRED: Signifies that this correction is necessary.  

* -NONE-: Placeholder, typically for additional flags or notes.    

* 0: Confidence score or priority level (if applicable).    
---
## Type of annotation 
---  
- **Edit**:  
Annotation: A 0 1|||Edit|||إلى|||REQUIRED|||-NONE-|||0  
Explanation: Change the text at position 0 to "إلى".  

- **Delete**:  
Annotation: A 39 40|||Delete||||||REQUIRED|||-NONE-|||0  
Explanation: Remove the text between positions 39 and 40.  

- **Add_before**:  
Annotation: A 4 4|||Add_before|||:|||REQUIRED|||-NONE-|||0  
Explanation: Insert a colon (:) before the text at position 4.  

- **Add_after**:  
Annotation: A 62 62|||Add_after|||؟|||REQUIRED|||-NONE-|||0  
Explanation: Insert a question mark (?) after the text at position 62.  

- **Merge**:  
Annotation: A 6 8|||Merge|||ومن|||REQUIRED|||-NONE-|||0  
Explanation: Combine the text from positions 6 to 8 into "ومن".  

- **Split**:  
Annotation: A 43 44|||Split|||لا فرق|||REQUIRED|||-NONE-|||0  
Explanation: Split the text at positions 43 to 44 into separate parts.  

- **Move**:  
Annotation: A 30 32|||Move|||هؤلاء الإرهابيون|||REQUIRED|||-NONE-|||0  
Explanation: Move the text "هؤلاء الإرهابيون" from positions 30 to 32 to another location in the text.  

- **Other**:  
Annotation: A 22 24|||Other|||وما الذي|||REQUIRED|||-NONE-|||0  
Explanation: This represents an unspecified or unique correction action involving the text "وما الذي" between positions 22 and 24.  
---



## Data Access
---
To access the datasets you had to request it from the following link:
- Qalb Dataset: [Click To Request](https://docs.google.com/forms/d/e/1FAIpQLScSsuAu1_84KORcpzOKTid0nUMQDZNQKKnVcMilaIZ6QF-xdw/viewform)
---
