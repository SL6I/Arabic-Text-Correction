## Dataset Contents

### Train
- **Files:**
  - **QALB-2014-L1-Train.sent**  
    Contains **19,411** original Arabic sentences, each representing a training example.
  - **QALB-2014-L1-Train.cor**  
    Contains the **corrected** versions of the sentences in **Train.sent**. Each line corresponds to the corrected form of the respective sentence in the `.sent` file.
  - **QALB-2014-L1-Train.m2**  
    Provides **detailed error annotations** for each sentence in **Train.sent**, following the M2 format (error type, position, and correction).
  - **QALB-2014-L1-Train.column**  
    Offers a **columnar view** that merges data from `.sent`, `.cor`, and `.m2` files for easier parsing and analysis.

- **Description:**  
  The **training set** is used to develop Arabic grammatical error correction models. It includes a substantial number of original sentences paired with corrections and error annotations, allowing models to learn common grammatical mistakes and their appropriate remedies.

---

### Development (Dev)
- **Files:**
  - **QALB-2014-L1-Dev.sent**  
    Contains **2,000** original Arabic sentences for validation purposes.
  - **QALB-2014-L1-Dev.cor**  
    Contains the **corrected** versions of the sentences in **Dev.sent**, aligned line by line.
  - **QALB-2014-L1-Dev.m2**  
    Provides **detailed error annotations** in M2 format for each sentence in **Dev.sent**.
  - **QALB-2014-L1-Dev.column**  
    A **column-based** file combining `.sent`, `.cor`, and `.m2` data for convenient reference.

- **Description:**  
  The **development set** is used to fine-tune model parameters and evaluate intermediate performance. It helps prevent overfitting and ensures good generalization to unseen data.

---

### Test
- **Files:**
  - **QALB-2014-L1-Test.sent**  
    Contains **2,500** original Arabic sentences for final evaluation.
  - **QALB-2014-L1-Test.cor**  
    Contains the **corrected** versions of the sentences in **Test.sent**, each on a separate line.
  - **QALB-2014-L1-Test.m2**  
    Offers **detailed error annotations** (M2 format) for each sentence in **Test.sent**.
  - **QALB-2014-L1-Test.column**  
    Provides a **columnar view** merging `.sent`, `.cor`, and `.m2` for the test set.


- **Description:**  
  The **test set** is used to evaluate the final performance of trained models, offering an unbiased assessment of how effectively they correct grammatical errors in new, unseen Arabic text.

## Sample Data


**S إلياهو فينوغراد يتنبأ بسيل من الهجمات الإيرانية واللني إما ستسقط فوق مناطق العرب وبعض البنايات الخاليه أو تصوير لبعض الجثث الحيه وهي تنقل فوق الطائرات وغيرها من فبركات هوليووديه إعلاميه . العداء الإيراني ليس إلا نموذج من الكذب الممنهج على طريقة النازي هتلر .**  
`A 7 8|||Edit|||والتي|||REQUIRED|||-NONE-|||0`  
`A 15 16|||Edit|||الخالية|||REQUIRED|||-NONE-|||0`  
`A 20 21|||Edit|||الحية|||REQUIRED|||-NONE-|||0`  
`A 28 29|||Edit|||هوليوودية|||REQUIRED|||-NONE-|||0`  
`A 29 30|||Edit|||إعلامية|||REQUIRED|||-NONE-|||0`  
`A 35 36|||Edit|||نموذجا|||REQUIRED|||-NONE-|||0`  

A: Denotes an annotation.

7 8: Range of index in the text where the correction is applied. This correction changes the word at indexes 7 to 8.

Edit: Type of annotation, indicating a modification of existing content.  

<span dir="rtl">**والتي**: Corrected content to replace the original.</span>

REQUIRED: Signifies that this correction is necessary.  

-NONE-: Placeholder, typically for additional flags or notes.    

0: Confidence score or priority level (if applicable).    




## Data Access
To access the datasets for training, validation, and testing, use the following links:
- Training Data: [Click To Download](https://drive.google.com/file/d/1nWCQAENGr2TGC_27vz1NzteqmuXlTDx7/view?usp=sharing)
- Validation Data: [Click To Download](https://drive.google.com/file/d/1h8I0qNsNz1OfRzUQEahB8Zpiqyzi3OmB/view?usp=sharing)
- Testing Data: [Click To Download](https://drive.google.com/file/d/1EQuXoM3Tj5bZqsZxYBakhZ7ZNbFH-1LB/view?usp=sharing)

