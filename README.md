# NLP-for-Political-Leaning-Detection
# Political Text Classification with Naive Bayes

This project applies Natural Language Processing (NLP) and a Naive Bayes classifier to identify political party affiliation based on text data from convention speeches and congressional tweets. The project explores which words most strongly distinguish Republican and Democratic language styles, using cleaned and tokenized word frequencies as features.

---

## Project Structure

- `2020_Conventions.db` – SQLite DB containing party convention speeches
- `congressional_data.db` – SQLite DB with congressional candidate tweets
- `Module 4-Political Naive Bayes.ipynb` – Main notebook for data extraction, modeling, and evaluation
- `requirements.txt` – Python packages required

---
##  Features

- Extracts and processes political text from databases
- Tokenizes and cleans text using `nltk`
- Builds a Naive Bayes classifier on speech text
- Applies the model to real congressional tweets (2018)
- Shows most informative features and party classification accuracy
- Highlights misclassifications for further analysis

---

##  Technologies Used

- Python 3.11+
- SQLite3
- NLTK
- NumPy
- Jupyter Notebook

---
