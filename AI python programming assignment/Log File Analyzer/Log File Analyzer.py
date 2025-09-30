from collections import defaultdict

def analyze_log(input_file, output_file):
    error_counts = defaultdict(int)

    with open(input_file, "r") as f:
        for line in f:
            if "ERROR" in line:
                date = line.split()[0]  # assumes YYYY-MM-DD ...
                error_counts[date] += 1

    with open(output_file, "w") as f:
        f.write("Error Summary Report\n")
        f.write("====================\n\n")
        for date, count in sorted(error_counts.items()):
            f.write(f"{date}: {count} errors\n")

    print(f"✅ Report written to {output_file}")


if __name__ == "__main__":
    analyze_log("app.log", "error_summary.txt")
