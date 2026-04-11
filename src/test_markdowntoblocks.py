import unittest
from markdown_blocks import markdown_to_blocks
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


if __name__ == "__main__":
    unittest.main()