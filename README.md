# AI-python-programming-assignment
 assignment &amp; capstone of AI python programming
AI Pair Programming with GitHub Copilot
Python Exercises for Senior Engineers (Built-in Libraries Only)
1. Log File Analyzer
- Read a `.log` file line by line
- Extract lines with 'ERROR' and group them by date (YYYY-MM-DD)
- Count total errors per day
- Output a summary report to a `.txt` file
2. Mini CSV Data Aggregator
- Use a list of dictionaries to simulate a CSV dataset
- Each record contains `name`, `age`, and `city`
- Group by city and compute:
 - Average age per city
 - Total number of residents
3. Text Analyzer
- Accept a paragraph of text from user input
- Calculate:
 - Total number of words
 - Most frequent word
 - Average word length
- Remove punctuation using `str.translate`
4. Recursive File System Explorer
- Use `os.walk()` to recursively explore directories
- Find all `.py` files and list them with their sizes
- Sort results by size in descending order
5. Custom Deck of Cards Simulator
- Create a 52-card deck using list of tuples (`rank`, `suit`)
- Shuffle using `random.shuffle`
- Simulate drawing `n` cards
- Show card distribution by suits

Capstone Project 1: AI-powered Resume Screener

 

Requirements specification:

 

Build a Python application that takes in a set of resumes (text or PDF format) and job descriptions, then uses NLP to rank the resumes based on how well they match the job requirements.

 

Functional Requirements

 

Parse resumes in .txt or .pdf format.

 

Input a job description (via GUI or command line).

 

Tokenize and vectorize text (TF-IDF or transformer-based).

 

Compute similarity score between resumes and job description.

 

Return the top N ranked resumes.

 

Suggestions for participants

 

Use PyPDF2 or pdfminer.six for PDF parsing.

 

Apply scikit-learn's TfidfVectorizer or SentenceTransformer for embeddings.

 

Use cosine_similarity to compute match scores.

 

Incorporate logging and modular design for testing.

 

Use AI pair programming tools to generate helper functions, e.g., text cleaning, parsing.

 

---------------------------------------------------------------------------------- 

----------------------------------------------------------------------------------
