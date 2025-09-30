import string
from collections import Counter

def analyze_text(input_file, output_file):
    with open(input_file, "r") as f:
        text = f.read()

    # remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator)

    words = clean_text.split()
    total_words = len(words)
    avg_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    most_common_word, freq = Counter(words).most_common(1)[0]

    with open(output_file, "w") as f:
        f.write("Text Analysis Report\n")
        f.write("====================\n\n")
        f.write(f"Total Words: {total_words}\n")
        f.write(f"Most Frequent Word: {most_common_word} ({freq} times)\n")
        f.write(f"Average Word Length: {round(avg_length,2)}\n")

    print(f"✅ Report written to {output_file}")


if __name__ == "__main__":
    analyze_text("paragraph.txt", "text_summary.txt")
