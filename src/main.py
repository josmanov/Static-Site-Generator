from textnode import TextNode

def main():
    text = "This is some anchor text"
    text_type = "link"
    url = "https://www.boot.dev"
    result = TextNode(text, text_type, url)

if __name__ == "__main__":
    main()