from enum import Enum
from htmlnode import ParentNode
from textnode import text_node_to_html_node
from splitnodes import text_to_textnodes
from textnode import TextNode, TextType




import re

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        block = block.strip()
        if block:
            blocks.append(block)

    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif all(re.match(r"^\d+\. ", line) for line in block.split("\n")):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            html_nodes.append(heading_to_html(block))
        elif block_type == BlockType.CODE:
            html_nodes.append(code_to_html(block))
        elif block_type == BlockType.QUOTE:
            html_nodes.append(quote_to_html(block))
        elif block_type == BlockType.UNORDERED_LIST:
            html_nodes.append(unordered_to_html(block))
        elif block_type == BlockType.ORDERED_LIST:
            html_nodes.append(ordered_to_html(block))
        else:
            html_nodes.append(paragraph_to_html(block))
    return html_nodes

def heading_to_html(text):
    hashtag_count = 0
    for char in text:
        if char == "#":
            hashtag_count += 1
        else:
            break
    strip_text = text.strip("# ")
    children = text_to_children(strip_text)
    return ParentNode(f"h{hashtag_count}", children)

def code_to_html(text):
    strip_text = text.removeprefix("```").removesuffix("```")
    node = TextNode(strip_text, TextType.CODE)
    return ParentNode("pre", [text_node_to_html_node(node)])

def quote_to_html(text):
    lines = text.split("\n")
    clean_lines = []
    for line in lines:
        clean_lines.append(line.lstrip("> "))
    quote_text = " ".join(clean_lines)
    children = text_to_children(quote_text)
    return ParentNode("blockquote", children)

def unordered_to_html(text):
    items = []
    for line in text.split("\n"):
        item_text = line[2:]
        items.append(ParentNode("li", text_to_children(item_text)))
    return ParentNode("ul", items)

def ordered_to_html(text):
    items = []
    for line in text.split("\n"):
        item_text = re.sub(r"^\d+\. ", "", line)
        items.append(ParentNode("li", text_to_children(item_text)))
    return ParentNode("ol", items)

def paragraph_to_html(text):
    hashtag_count = 0
    for char in text:
        if char == "#":
            hashtag_count += 1
        else:
            break
    strip_text = text.strip("# ")
    children = text_to_children(strip_text)
    return ParentNode(f"h{hashtag_count}", children)

def text_to_children(text):
    nodes = []
    for text_node in text_to_textnodes(text):
        nodes.append(text_node_to_html_node(text_node))
    return nodes

print(markdown_to_html_node("``` Hello World ```"))