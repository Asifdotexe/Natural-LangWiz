# Natural LangWiz 🧙‍♂️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Libraries](https://img.shields.io/badge/Libraries-Transformers%20%7C%20spaCy%20%7C%20NLTK%20%7C%20Scikit--learn-orange)
![Concepts Practiced](https://img.shields.io/badge/Concepts%20Practiced-24-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Welcome to **Natural LangWiz**!

Inspired from the book *"Skip the Line"*, where James Altucher champions the idea that mastery comes from doing **10,000 experiments** rather than just putting in 10,000 hours. This repository embraces that philosophy by treating each notebook and script as a distinct experiment in the vast and fascinating world of Natural Language Processing (NLP).

This collection contains **24 unique NLP experiments**, each designed to build practical skills and deepen understanding. Let's get experimenting!

***

## 🚀 Setup and Installation

### Prerequisites
- **Python 3.10+**
- **Poetry** (Package Manager) - [Installation Guide](https://python-poetry.org/docs/#installation)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Asifdotexe/Natural-LangWiz.git
    cd Natural-LangWiz
    ```

3.  **Install dependencies:**
    ```bash
    poetry install
    ```

### Running the Code
- **Run a script:**
  ```bash
  poetry run python code/main.py
  ```
- **Launch Jupyter Notebooks:**
  ```bash
  poetry run jupyter notebook
  ```

***

## 🧪 NLP Experiments & Notebooks

| Category | Concept & Notebook | Description |
| :--- | :--- | :--- |
| **Fundamentals** | **[Data Preprocessing](code/nlp_data_processing.ipynb)** | Covers essential text cleaning, tokenization, stop-word removal, stemming, and lemmatization. |
| **Fundamentals** | **[Vectorization](code/nlp_vectorizer.ipynb)** | Demonstrates converting text to numbers using Bag-of-Words (BoW) and TF-IDF. |
| **Fundamentals** | **[N-Grams](code/nlp_n_grams.ipynb)** | Implements n-grams to analyze contiguous sequences of words in text. |
| **Sentiment Analysis** | **[AFINN Sentiment Analysis](code/nlp_affin_sentimental_analysis.ipynb)** | Performs lexicon-based sentiment analysis using the AFINN library. |
| **Sentiment Analysis** | **[VADER Sentiment Analysis](code/nlp_sentimental_analysis.ipynb)** | Utilizes VADER for rule-based sentiment analysis on social media text. |
| **Sentiment Analysis** | **[Emotion Analysis (Transformer)](code/nlp_transformer_emotion_analysis.ipynb)** | Uses a transformer model to detect specific emotions like joy, disgust, etc. |
| **Transformer Models** | **[Text Summarization](code/nlp_transformer_summarization.ipynb)** | Generates concise summaries of long texts using a transformer pipeline. |
| **Transformer Models** | **[Text Generation](code/nlp_transformer_text_generation.ipynb)** | Leverages the GPT-2 model to generate coherent text from a given prompt. |
| **Transformer Models** | **[Question Answering](code/nlp_question_answering_model.ipynb)** | Implements a QA system with a RoBERTa model to find answers within a context. |
| **Core Applications** | **[Named Entity Recognition (NER)](code/nlp_name_entity_recognition.ipynb)** | Uses spaCy to identify and classify entities like people, organizations, and locations. |
| **Core Applications** | **[Spam Detection](code/nlp_spam_detection.ipynb)** | Builds a model to classify SMS messages as spam or not spam (ham). |
| **Core Applications**| **[Topic Modelling](code/nlp_topic_modelling.ipynb)** | Discovers abstract topics in a corpus using Latent Dirichlet Allocation (LDA). |
| **Text Comparison** | **[Similarity Checker](code/nlp_similarity_checker.ipynb)** | Calculates semantic similarity between words and sentences using spaCy and WordNet. |
| **Text Comparison** | **[Fuzzy Matching](code/nlp_fuzzy_matching.ipynb)** | Implements fuzzy string matching to find similarities between non-identical strings. |
| **Text Correction** | **[Grammar Checking](code/nlp_grammar_checker.ipynb)** | Implements a grammar and spelling checker using `language-tool-python`. |
| **Specialized Tools** | **[Demojification](code/nlp_demojification.ipynb)** | Handles emojis by either removing them or replacing them with text descriptions. |
| **Specialized Tools** | **[Translation](code/nlp_translator.ipynb)** | A simple script to translate text between languages using the Google Translate API. |
| **Specialized Tools** | **[Optical Character Recognition (OCR)](code/nlp_image_pytesseract.ipynb)** | An experiment in extracting text from images using `pytesseract`. |
| **API Integration** | **[Python Gemini Integration](code/nlp_gemini_python_integration.ipynb)** | Shows how to interact with Google's Gemini API within a Python notebook. |
| **API Integration** | **[Gemini TKinter Script](code/prompt_generator_tkinter.py)** | A simple desktop GUI application to chat with the Gemini model. |
| **Misc. Scripts** | **[Review Insights Extractor](code/main.py)** | A practical script that analyzes product reviews to extract positive/negative aspects. |
| **Misc. Scripts** | **[Web Scraping](code/nlp_web_scraping.ipynb)** | Extracts data from Wikipedia and Amazon using Beautiful Soup. |
| **Misc. Scripts** | **[Word Cloud](code/nlp_word_cloud.ipynb)**| Creates a visual representation of text data based on word frequency. |
| **Misc. Scripts** | **[API Calling](code/nlp_api_calling.ipynb)** | Demonstrates how to interact with external APIs to retrieve and use text data. |

***

Happy Learning!
