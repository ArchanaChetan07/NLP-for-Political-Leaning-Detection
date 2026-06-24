import pytest
import re
from collections import Counter


class TestPoliticalTextProcessing:

    def test_text_cleaning(self):
        text = "  Conservative  policies  are  great!!! "
        clean = re.sub(r'[^a-zA-Z\s]', '', text).strip().lower()
        assert '!' not in clean
        assert clean == clean.lower()

    def test_political_keyword_detection(self):
        left_keywords = {"progressive", "equality", "climate", "healthcare", "regulation"}
        right_keywords = {"conservative", "freedom", "deregulation", "tradition", "taxcuts"}
        text = "We need progressive healthcare policies and climate action"
        tokens = set(text.lower().split())
        left_score = len(tokens & left_keywords)
        right_score = len(tokens & right_keywords)
        assert left_score > right_score

    def test_balanced_corpus_check(self):
        labels = ["left"] * 100 + ["right"] * 95 + ["center"] * 105
        counts = Counter(labels)
        total = sum(counts.values())
        for label, count in counts.items():
            assert 0.2 < count / total < 0.5

    def test_tfidf_vector_nonzero(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        docs = ["conservative policy freedom", "progressive healthcare equality", "moderate centrist bipartisan"]
        vec = TfidfVectorizer()
        X = vec.fit_transform(docs)
        assert X.nnz > 0

    def test_classification_output_valid(self):
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.feature_extraction.text import TfidfVectorizer
        docs = ["freedom taxes conservative"] * 20 + ["healthcare climate progressive"] * 20
        labels = ["right"] * 20 + ["left"] * 20
        vec = TfidfVectorizer()
        X = vec.fit_transform(docs)
        model = MultinomialNB()
        model.fit(X, labels)
        preds = model.predict(X)
        assert set(preds).issubset({"left", "right"})
