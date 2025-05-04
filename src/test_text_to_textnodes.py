import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import text_to_textnodes

basic_text_all = "This is **bold text** with an _italic word_ and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
basic_text_no_bold = "This is an _italic word_ and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"


class TestTextNode(unittest.TestCase):   
    
    def test_all_types_simple(self):
        """Tests for correct extraction of the example text from the lesson!"""
        result = text_to_textnodes(basic_text_all)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic word", TextType.ITALIC),
                TextNode(" and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )

    def test_all_types_no_bold_simple(self):
        """Tests for correct extraction of the example text from the lesson, without the BOLD section"""
        result = text_to_textnodes(basic_text_no_bold)
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("italic word", TextType.ITALIC),
                TextNode(" and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )
    
    
    

if __name__ == "__main__":
    unittest.main()