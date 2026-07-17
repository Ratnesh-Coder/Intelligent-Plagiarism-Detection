# ============================================================
# TEXT PREPROCESSING
# ============================================================

import nltk
import string

def preprocess_text(text):
    """
    Normalize text by:
    - Lowercasing
    - Removing stopwords
    - Removing punctuation
    """

    tokens = nltk.word_tokenize(text.lower())

    cleaned_tokens = []

    for word in tokens:

        if word not in string.punctuation:
            cleaned_tokens.append(word)

    return " ".join(cleaned_tokens)