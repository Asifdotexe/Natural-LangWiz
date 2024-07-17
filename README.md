# MachineUnderstandsTextData

Welcome to theMachineUnderstandsTextData Repository! This repository contains Jupyter notebooks that cover various fundamental concepts and techniques in Natural Language Processing (NLP). Each notebook is designed to be self-contained, providing explanations and examples to help you understand and implement basic NLP tasks.

## Table of Contents

1. [Data Preprocessing](#data-preprocessing)
   - [Text Cleaning](#text-cleaning)
   - [Converting Text to Lowercase](#converting-text-to-lowercase)
   - [Removing Whitespace and Non-Textual Characters](#removing-whitespace-and-non-textual-characters)
   - [Removing Digits](#removing-digits)
   - [Tokenization](#tokenization)
   - [Stemming](#stemming)
   - [Lemmatization](#lemmatization)
   - [Part of Speech Tagging](#part-of-speech-tagging)
2. [Web Scraping](#web-scraping)
   - [Wikipedia Scraping using Beautiful Soup](#wikipedia-scraping-using-beautiful-soup)
   - [Amazon Scraping using Beautiful Soup](#amazon-scraping-using-beautiful-soup)
3. [Word Cloud](#word-cloud)
4. [Emojification](#emojification)
   - [Removing Emojis](#removing-emojis)
   - [Replacing Emojis with Text](#replacing-emojis-with-text)

## Data Preprocessing

Data preprocessing is a crucial step in NLP to clean and prepare text data for analysis and modeling. The following preprocessing steps are covered in the [Data Preprocessing Notebook](https://github.com/Asifdotexe/MachineUnderstandsTextData/blob/main/nlp_data_processing.ipynb):

### Text Cleaning
Using regular expressions (regex), unwanted characters and patterns are removed from the text to make it clean and uniform.

### Converting Text to Lowercase
Converts all characters in the text to lowercase to ensure uniformity and avoid case sensitivity issues during analysis.

### Removing Whitespace and Non-Textual Characters
Removes unnecessary whitespace and non-textual characters to streamline the text.

### Removing Digits
Digits are removed from the text to focus on the textual content.

### Tokenization
Splits the text into individual words or tokens, which are the basic units for further NLP tasks.

### Stemming
Reduces words to their base or root form by removing suffixes. For example, "running" becomes "run".

### Lemmatization
Similar to stemming, but more sophisticated. It reduces words to their dictionary form. For example, "running" becomes "run" and "better" becomes "good".

### Part of Speech Tagging
Identifies and labels the part of speech (e.g., noun, verb, adjective) for each token in the text.

## Web Scraping

Web scraping is the process of extracting data from websites. The following web scraping tasks are covered in the [Web Scraping Notebook](https://github.com/Asifdotexe/MachineUnderstandsTextData/blob/main/nlp_web_scraping.ipynb):

### Wikipedia Scraping using Beautiful Soup
Extracts data from Wikipedia pages using the Beautiful Soup library.

### Amazon Scraping using Beautiful Soup
Extracts product data from Amazon using the Beautiful Soup library.

## Word Cloud

A word cloud is a visual representation of text data, where the size of each word indicates its frequency or importance. The [Word Cloud Notebook](https://github.com/Asifdotexe/MachineUnderstandsTextData/blob/main/nlp_word_cloud.ipynb) demonstrates how to create a word cloud from a given corpus.

## Emojification

Emojification involves handling emojis in text data, either by removing them or replacing them with corresponding text. The following tasks are covered in the [Emojification Notebook](https://github.com/Asifdotexe/MachineUnderstandsTextData/blob/main/nlp_demojification.ipynb):

### Removing Emojis
Uses the `demoji` library to identify and remove emojis from the text.

### Replacing Emojis with Text
Uses the `emoji` library to replace emojis with their corresponding text descriptions.

---

Feel free to explore the notebooks and enhance your understanding of basic NLP concepts. If you have any questions or suggestions, please open an issue or submit a pull request.

Happy Learning!


