import unittest

from splitnodes import extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            " and also another ![image](https://i.imgur.com/5555jxJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),
                              ("image", "https://i.imgur.com/5555jxJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](www.google.com)"
        )
        self.assertListEqual([("link", "www.google.com")], matches)

        matches = extract_markdown_links(
            "This is text with an [link](www.google.com)"
            " and also another text with an [link](www.wikipedia.com)"
        )
        self.assertListEqual([("link", "www.google.com"),
                              ("link", "www.wikipedia.com")], matches)

    