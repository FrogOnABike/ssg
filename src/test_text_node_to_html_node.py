import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    # **** Tests for text_node_to_html_node ****
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")
        
    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
        
    def test_link(self):
        node = TextNode("This is a link!", TextType.LINK,"http://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link!")
        self.assertEqual(html_node.props, {"href":"http://www.google.com"})

    def test_image(self):
        node = TextNode("This is an image link!", TextType.IMAGE,"https://picsum.photos/200")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://picsum.photos/200","alt":"This is an image link!"})
       
    def test_invalid(self):
        with self.assertRaises(Exception):
            node = TextNode("This is an invalid node", TextType.DUMMY)
            html_node = text_node_to_html_node(node)
    
if __name__ == "__main__":
    unittest.main()