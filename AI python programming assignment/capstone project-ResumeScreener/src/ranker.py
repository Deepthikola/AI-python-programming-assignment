from vectorizer import TfidfEmbedder

def rank_resumes(resume_texts: list[str], job_desc: str, top_n: int = 5):
    """
    Return list of (index, score) for the top_n resumes matching job_desc.
    """
    embedder = TfidfEmbedder()
    doc_mat   = embedder.fit_transform(resume_texts)
    query_vec = embedder.transform(job_desc)
    scores    = embedder.similarity(doc_mat, query_vec)
    ranked_ix = scores.argsort()[::-1][:top_n]
    return [(int(i), float(scores[i])) for i in ranked_ix]
