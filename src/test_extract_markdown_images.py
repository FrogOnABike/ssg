import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import extract_markdown_images

class TestTextNode(unittest.TestCase):   
            
    # *** Tests for extract_markdown_images ***
    
    def test_extract_markdown_images_simple(self):
        """Test basic extraction for single item pair"""
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_images_pair(self):
        """Test basic extraction for a pair of images"""
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
        
    def test_extract_markdown_images_invalid_format_simple_at(self):
        """Test extraction doesn't return anything if invalid format (missing ! for alt_text)"""
        matches = extract_markdown_images(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_invalid_format_simple_url(self):
        """Test extraction doesn't return anything if invalid format (missing ( for url)"""
        matches = extract_markdown_images(
            "This is text with an ![image]https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([], matches)
        
    def test_extract_markdown_images_invalid_format_pair(self):
        """Test basic extraction for a pair, one with invalid format - should only return valid one"""
        matches = extract_markdown_images(
            "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    )
        self.assertListEqual([("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
        
    def test_extract_markdown_images_empty_string(self):
        """Test when input is an empty string"""
        matches = extract_markdown_images(
            ""
    )
        self.assertListEqual([], matches)
        
    def test_extract_markdown_images_nested_brackets(self):
        """Test basic extraction for single item pair"""
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
if __name__ == "__main__":
    unittest.main()