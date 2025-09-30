def extract_text_from_txt(path: str) -> str:
    """
    Read a plain-text file and return its contents.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
