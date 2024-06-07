import os

def format_title(file_name):
    name_without_ext = os.path.splitext(file_name)[0]
    words = name_without_ext.split('_')
    formatted_name = ' '.join(word.capitalize() for word in words)
    return formatted_name

def update_readme(directory):
    readme_path = os.path.join(directory, "README.md")
    md_files = [f for f in os.listdir(directory) if f.endswith(".md") and f != "README.md"]

    if not md_files:
        return

    with open(readme_path, "w") as readme_file:
        readme_file.write("# 📚 Contents\n\n")
        for md_file in md_files:
            title = format_title(md_file)
            readme_file.write(f"- [{title}]({md_file})\n")

def generate_repo_structure(path=".", indent=0):
    items = []
    for item in sorted(os.listdir(path)):
        if item.startswith('.'):
            continue
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            folder_name = item
            items.append(f'{"  " * indent}- 📂 {folder_name}')
            items.extend(generate_repo_structure(full_path, indent + 1))
        elif full_path.endswith(".md") and not full_path.endswith("README.md"):
            title = format_title(item)
            items.append(f'{"  " * indent}- 📄 [{title}]({full_path})')
    return items

def update_root_readme():
    structure = generate_repo_structure()
    structure_content = "# 📚 Contents\n\n" + "\n".join(structure)

    readme_path = "README.md"
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as readme_file:
            readme_file.write(structure_content)
        return

    with open(readme_path, "r") as readme_file:
        lines = readme_file.readlines()

    with open(readme_path, "w") as readme_file:
        in_contents_section = False
        for line in lines:
            if line.strip() == "<!-- CONTENTS -->":
                readme_file.write(line)
                readme_file.write(structure_content + "\n")
                in_contents_section = True
            elif line.strip() == "<!-- END CONTENTS -->":
                readme_file.write(line)
                in_contents_section = False
            elif not in_contents_section:
                readme_file.write(line)

def main():
    # Update README files in subdirectories
    for root, dirs, files in os.walk("."):
        if root == ".":
            continue
        update_readme(root)
    
    # Update README file in the root directory
    update_root_readme()

if __name__ == "__main__":
    main()
