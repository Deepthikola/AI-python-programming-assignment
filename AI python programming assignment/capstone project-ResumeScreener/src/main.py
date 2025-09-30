# src/main.py

import os
from pdf_parser import extract_text_from_pdf
from txt_parser import extract_text_from_txt
from ranker import rank_resumes

# 1. Paths
SRC_DIR     = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath(os.path.join(SRC_DIR, os.pardir))
INPUT_DIR   = os.path.join(PROJECT_DIR, "inputs")
JOB_FILE    = os.path.join(PROJECT_DIR, "job.txt")
OUTPUT_FILE = os.path.join(PROJECT_DIR, "ranked_resumes.txt")

def main():
    # 2. Load job description
    if not os.path.isfile(JOB_FILE):
        print(f"Error: could not find job description at {JOB_FILE}")
        return
    job_desc = extract_text_from_txt(JOB_FILE)

    # 3. Collect all resumes in inputs/
    files = sorted(os.listdir(INPUT_DIR))
    resumes = [f for f in files if f.lower().endswith((".txt", ".pdf"))]
    if not resumes:
        print("Error: no .txt or .pdf resumes found in inputs/")
        return

    # 4. Parse each resume (skip any failures)
    parsed_texts = []
    parsed_names = []
    for fname in resumes:
        path = os.path.join(INPUT_DIR, fname)
        try:
            text = (
                extract_text_from_pdf(path)
                if fname.lower().endswith(".pdf")
                else extract_text_from_txt(path)
            )
            if text.strip():
                parsed_texts.append(text)
                parsed_names.append(fname)
            else:
                print(f"Warning: no text extracted from {fname}, skipping")
        except Exception as e:
            print(f"Warning: skipping {fname} ({e})")

    if not parsed_texts:
        print("Error: no valid resumes to rank")
        return

    # 5. Rank them all
    results = rank_resumes(parsed_texts, job_desc, top_n=len(parsed_texts))

    # 6. Write out ranked_resumes.txt
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("Rank\tFilename\tScore\n")
        for rank, (idx, score) in enumerate(results, start=1):
            out.write(f"{rank}\t{parsed_names[idx]}\t{score:.4f}\n")

    print(f"✅ Wrote {len(parsed_texts)} scores to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
