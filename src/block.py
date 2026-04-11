from enum import Enum
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