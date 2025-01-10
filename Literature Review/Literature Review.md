### Author
1- Bashar Alhafni
2- Go Inoue
3- Christian Khairallah
4- Nizar Habash

### Title of paper
Advancements in Arabic Grammatical Error Detection and Correction: An Empirical Investigation

### Publication venue
Abu Dhabi, UAE

### year of publication
2023

### number of pages
19

### Description
* In This paper, the authors present the first results on Arabic grammatical error correction (GEC) using two newly developed Transformer-based pre-trained sequence-to-sequence models. They also introduce a new multi-class Arabic grammatical error detection (GED) task and develop corresponding models. By incorporating GED information as auxiliary input, the authors improve GEC performance across diverse datasets covering different genres and proficiency levels. Additionally, they also leverage contextual morphological preprocessing to further enhance GEC model performance. 
* Their experiments demonstrate significant improvements over previous state-of-the-art systems on established Arabic GEC shared task datasets, while also establishing a strong benchmark on a recently developed dataset. This comprehensive evaluation, coupled with making their code, data, and pre-trained models publicly available, provides a solid foundation for future research on Arabic GEC and GED.

### explanation
* We are implementing a paper that introduces a Transformer-based model for Arabic Grammatical Error Correction (GEC). This is the first study to use newly developed Transformer models for Arabic GEC and to introduce a multi-class grammatical error detection (GED) task. The authors improve GEC performance by using GED information as an extra input and applying contextual morphological preprocessing. Their approach achieves better results than previous models on multiple datasets, including QALB-2014, QALB-2015, and a new dataset called ZAEBUC.
* We will take MLE as a great choice because it has the highest precision, good recall, and a strong F₀.₅ score, making it very reliable for Arabic GEC. If you want accurate corrections with fewer mistakes, MLE is the best option.
  
