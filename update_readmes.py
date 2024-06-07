import os

def update_readme(directory):
    readme_path = os.path.join(directory, "README.md")
    md_files = [f for f in os.listdir(directory) if f.endswith(".md") and f != "README.md"]

    if not md_files:
        return

    with open(readme_path, "w") as readme_file:
        readme_file.write("# Contents\n\n")
        for md_file in md_files:
            readme_file.write(f"- [{md_file}]({md_file})\n")

def main():
    for root, dirs, files in os.walk("."):
        if root == ".":
            continue
        update_readme(root)

if __name__ == "__main__":
    main()
