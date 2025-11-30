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
- Neural baseline (BiLSTM)

**Results:**  
- LinearSVC: 98.97% accuracy  
- BiLSTM: ~42% accuracy  
- ~6 points higher accuracy than reported BERTAA (~93%)

**Skills:** Feature engineering, scikit-learn, TensorFlow, spaCy, model evaluation  
**Repo:** [imdb62-authorship-attribution](https://github.com/jingyingx/imdb62-authorship-attribution)

