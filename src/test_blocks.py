import unittest
from block import markdown_to_blocks, block_to_block_type, BlockType, quote_to_html, unordered_to_html, ordered_to_html, paragraph_to_html, markdown_to_html_node

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

    def test_quote_to_html_single_line(self):
        node = quote_to_html("> this is a quote")
        self.assertEqual(node.to_html(), "<blockquote>this is a quote</blockquote>")

    def test_quote_to_html_multi_line(self):
        node = quote_to_html("> this is\n> a multiline quote")
        self.assertEqual(node.to_html(), "<blockquote>this is a multiline quote</blockquote>")

    def test_unordered_to_html(self):
        node = unordered_to_html("- first\n- second")
        self.assertEqual(node.to_html(), "<ul><li>first</li><li>second</li></ul>")

    def test_ordered_to_html(self):
        node = ordered_to_html("1. first\n2. second")
        self.assertEqual(node.to_html(), "<ol><li>first</li><li>second</li></ol>")

    def test_paragraph_to_html(self):
        node = paragraph_to_html("this is\na paragraph")
        self.assertEqual(node.to_html(), "<p>this is a paragraph</p>")

    def test_markdown_to_html_node_wraps_in_div(self):
        markdown = "Hello world"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><p>Hello world</p></div>")

    def test_markdown_to_html_node_multiple_blocks(self):
        markdown = "# Title\n\n> quote"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><h1>Title</h1><blockquote>quote</blockquote></div>")


if __name__ == "__main__":
    unittest.main()