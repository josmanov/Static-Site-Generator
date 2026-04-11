import unittest
from block import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]

        result = markdown_to_blocks(markdown)

        self.assertEqual(result, expected)

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Title"),
            BlockType.HEADING
        )
        self.assertEqual(
            block_to_block_type("###### Small heading"),
            BlockType.HEADING
        )

    def test_code(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_quote(self):
        block = "> hello\n> world"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

    def test_paragraph(self):
        block = "This is just a normal paragraph with text."
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()