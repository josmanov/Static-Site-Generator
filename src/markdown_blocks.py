def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        block = block.strip()
        if block:
            blocks.append(block)

    return blocks