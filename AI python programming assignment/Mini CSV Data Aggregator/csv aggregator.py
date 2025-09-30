import csv
from collections import defaultdict

def aggregate_csv(input_file, output_file):
    city_data = defaultdict(list)

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            city_data[row["city"]].append(int(row["age"]))

    with open(output_file, "w") as f:
        f.write("City Summary\n")
        f.write("============\n\n")
        for city, ages in city_data.items():
            avg_age = sum(ages) / len(ages)
            f.write(f"{city}: Average Age = {round(avg_age,2)}, Residents = {len(ages)}\n")

    print(f"✅ Summary written to {output_file}")


if __name__ == "__main__":
    aggregate_csv("people.csv", "city_summary.txt")
