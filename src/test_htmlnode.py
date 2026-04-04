import unittest

from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, None)
        node.props_to_html()
        node = HTMLNode(None, None, None, {"a": "https://www.google.com", "target": "_blank"})
        node.props_to_html()
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node.props_to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        print(node.to_html())


if __name__ == "__main__":
    unittest.main()