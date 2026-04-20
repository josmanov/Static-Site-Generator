from textnode import TextNode
import os
import shutil

def main():
    text = "This is some anchor text"
    text_type = "link"
    url = "https://www.boot.dev"
    result = TextNode(text, text_type, url)
    clear_public_dir("public")

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

if __name__ == "__main__":
    main()