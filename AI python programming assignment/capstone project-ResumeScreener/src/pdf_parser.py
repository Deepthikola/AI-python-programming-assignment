from pdfminer.high_level import extract_text as _extract_text_miner
from pdfminer.pdfparser import PDFSyntaxError
from PyPDF2 import PdfReader

def extract_text_from_pdf(path: str) -> str:
    """
    Try pdfminer first; if it fails on “bad” PDFs, try PyPDF2.
    """
    try:
        return _extract_text_miner(path)
    except PDFSyntaxError:
        # fallback to PyPDF2
        try:
            reader = PdfReader(path)
            text = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
            return "\n".join(text)
        except Exception as e2:
            raise RuntimeError(f"Both pdfminer and PyPDF2 failed for {path}: {e2}")
    except Exception as e:
        raise RuntimeError(f"pdfminer failed for {path}: {e}")
