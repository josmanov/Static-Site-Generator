from textnode import TextNode
import os
import shutil

def main():
    text = "This is some anchor text"
    text_type = "link"
    url = "https://www.boot.dev"
    result = TextNode(text, text_type, url)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    source_dir = os.path.join(script_dir, "static")
    dest_dir = os.path.join(repo_root, "public")
    clear_public_dir(dest_dir)
    copy_directory_recursive(source_dir, dest_dir)


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}"
    )

    with open(from_path, "r", encoding="utf-8") as markdown_file:
        markdown_contents = markdown_file.read()

    with open(template_path, "r", encoding="utf-8") as template_file:
        template_contents = template_file.read()

def clear_public_dir(public_dir):
    if not os.path.exists(public_dir):
        os.mkdir(public_dir)
        return

    for item in os.listdir(public_dir):
        item_path = os.path.join(public_dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        else:
            shutil.rmtree(item_path)


def copy_directory_recursive(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} -> {dest_path}")
        else:
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_directory_recursive(source_path, dest_path)

if __name__ == "__main__":
    main()