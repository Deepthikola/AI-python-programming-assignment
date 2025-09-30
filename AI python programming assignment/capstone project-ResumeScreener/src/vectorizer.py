from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TfidfEmbedder:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, docs: list[str]):
        """
        Learn vocabulary & idf, return TF-IDF matrix for docs.
        """
        return self.vectorizer.fit_transform(docs)

    def transform(self, doc: str):
        """
        Transform a single document into the existing TF-IDF space.
        """
        return self.vectorizer.transform([doc])

    def similarity(self, doc_matrix, query_vec):
        """
        Compute cosine similarity between each row in doc_matrix and query_vec.
        """
        return cosine_similarity(doc_matrix, query_vec).flatten()
