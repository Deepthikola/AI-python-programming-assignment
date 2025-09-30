import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """
    Lowercase, remove punctuation, and collapse whitespace.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def tokenize_text(text: str) -> list[str]:
    """
    Split cleaned text into tokens, filtering out stopwords.
    """
    tokens = word_tokenize(clean_text(text))
    return [t for t in tokens if t not in stop_words]
