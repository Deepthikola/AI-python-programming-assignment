import os

def explore(root_dir, output_file):
    py_files = []

    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".py"):
                full_path = os.path.join(dirpath, file)
                size = os.path.getsize(full_path)
                py_files.append((full_path, size))

    py_files.sort(key=lambda x: x[1], reverse=True)

    with open(output_file, "w") as f:
        f.write("Python Files (sorted by size)\n")
        f.write("=============================\n\n")
        for path, size in py_files:
            f.write(f"{path}: {size} bytes\n")

    print(f"✅ File list written to {output_file}")


if __name__ == "__main__":
    explore("..", "py_files.txt")   # scans parent directory of Problem4
