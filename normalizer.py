import re
import unicodedata
import spacy
from nltk.corpus import stopwords
from dateparser import parse as date_parse

# Load spaCy English model (make sure to install: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

class TextNormalizer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = set(stopwords.words("english"))

    def normalize_query(self, query: str) -> str:
        # 1. Unicode normalization
        query = unicodedata.normalize("NFKC", query)

        # 2. Lowercasing
        query = query.lower().strip()

        # 3. Remove extra spaces, punctuation (keep numbers & words)
        query = re.sub(r"[^a-z0-9\s]", " ", query)
        query = re.sub(r"\s+", " ", query)

        # 4. Lemmatization + stopword removal
        doc = nlp(query)
        tokens = []
        for token in doc:
            if token.text not in stop_words:
                tokens.append(token.lemma_)  # lemmatized form
        
        # 5. Entity normalization (dates, numbers, money, etc.)
        normalized_tokens = []
        for token in tokens:
            # Only try to parse as date if  is a known date word
            date_words = {"today", "tomorrow", "yesterday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"}
            if ( token in date_words):
                dt = date_parse(token)
                if dt:
                    normalized_tokens.append(dt.strftime("%Y-%m-%d"))
                    continue
            normalized_tokens.append(token)

        # 6. Named Entity Recognition (NER) - Optional, can be customized
        for ent in doc.ents:
            if ent.label_ in {"PERSON", "GPE", "LOC"}:
                normalized_tokens = [t for t in normalized_tokens if t not in ent.text.split()]
                normalized_tokens.append(ent.label_.lower())
        # 7. Re-join
        normalized_query = " ".join(normalized_tokens)
        return normalized_query


