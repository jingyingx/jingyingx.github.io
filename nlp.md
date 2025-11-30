---
layout: single
title: "NLP Portfolio"
permalink: /nlp/
author_profile: false
---


Welcome to my NLP portfolio, which highlights my applied NLP projects and critical readings of foundational NLP/LLM papers from both computational and linguistic perspectives. My goal is to combine rigorous linguistic theory with modern machine learning methods to better understand how NLP models interpret, structure, and learn from language.

## NLP/LLM Paper Critiques

I post updates on critiques of foundational NLP and LLM papers. The goal is to critically examine each paper’s assumptions, model design, and evaluation methodology. Rather than judging past work by modern standards, these critiques emphasize the specific problems each model was originally designed to solve. They also incorporate linguistic insights and highlight how a linguist’s perspective can deepen our understanding of NLP research.

- [*GPT or BERT: Why not both?* Charpentier & Samuel (2024)](http://jingyingx.github.io/critique_BabyLM.pdf) - winner of the 2nd BabyLM Challenge (2024).
- [*BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* (Devlin et al., 2019)](http://jingyingx.github.io/critique_bert.pdf) — the foundational BERT paper introducing bidirectional Transformer pretraining.
- [*Efficient Estimation of Word Representations in Vector Space* (Mikolov et al., 2013)](http://jingyingx.github.io/critique_word2vec.pdf) — introduction of the Word2Vec skip-gram and CBOW models.
- [*A Neural Probabilistic Language Model* (Bengio et al., 2003)](http://jingyingx.github.io/critique_neural.pdf) — early neural approach to language modeling prior to word embeddings.


## Featured Projects

### **1. Feature engineering > Big Models: Authorship Attribution on IMDb62**

The goal of this project is to show that **smart feature engineering + linear models** can outperform both naive neural models and transformer-based systems on stylometric authorship attribution tasks.

A high-performing, fully interpretable authorship attribution pipeline combining:
- Character TF–IDF  
- Word TF–IDF  
- Rich stylometric features
  - Discourse markers (and, but, however, though)
  - Punctuation style (commas, periods, quotes, dashes…)
  - Vocabulary richness (TTR, hapax)
  - POS-based lexical richness (VERB, ADJ, ADV)
  - Modal usage (can, will, would, may…)
  - Superlatives (“most”, “-est”)
  - Pronoun rates (1st and 2nd person)
  - Length/digit statistics (log length, digit ratio)
- LinearSVC classifier  
- BiLSTM neural baseline

**Results:**  
- LinearSVC: **98.97% accuracy**  
- BiLSTM: **~42% accuracy**  
- Outperforms reported BERTAA baseline by **~6 points** (~93%)

**Skills:** Feature engineering, scikit-learn, TensorFlow, spaCy, model evaluation  
**Repo:** [imdb62-authorship-attribution](https://github.com/jingyingx/imdb62-authorship-attribution)

<br><br>

### **2. Can Models Learn from Child Input Like Children Do? Verb Classification in Child Input (with Molly Thornber)**
This project investigates whether small, naturalistic child-directed speech contains enough information for a model to learn verb classes that children eventually master. The goal is to test **learnability**: Is there enough input for models trained on child-sized data to distinguish different verb types?

We analyzed **3,196 adult-to-child utterances** from the Brown corpus (CHILDES) and grouped 19 verbs into four intuitive classes (*eat*-type, *clean*-type, *open*-type, *carry*-type) based on the temporal structures of the events they describe. Each token was manually annotated with **14 syntactic and semantic features** and modeled using **linguistic features**, **DistilBERT embeddings**, and **combined features** with **SVM** and **FFNN** classifiers.

**Results:**  
- Only ***eat*-type** verbs were reliably learnable (F1 ≈ 0.69).
- Other classes (*open*, *clean*, *carry*) showed poor recoverability (F1 < 0.35).
- Two simple cues—**direct object presence** and **determiner-marked object**—were enough to classify *eat*-type verbs with high accuracy.

**Takeaway:**
Child-directed speech provides strong statistical cues for some verb types but not others, suggesting that children’s broader verb learning depends on more than input statistics alone (e.g., visual context, world knowledge, pragmatics).

**Skills:** Corpus construction, linguistic annotation, feature engineering, scikit-learn, DistilBERT embeddings, model evaluation

**Paper:** [*Verb Classification in Child Input: Can Models Learn from Child Input Like Children Do?*](http://jingyingx.github.io/verb_classifier.pdf)

