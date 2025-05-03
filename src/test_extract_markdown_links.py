import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import extract_markdown_links

class TestTextNode(unittest.TestCase):   
                    
    # *** Tests for extract_markdown_links ***
    
    def test_extract_markdown_links_simple(self):
        """Test basic extraction for single item pair"""
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
    )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
    
    def test_extract_markdown_links_pair(self):
        """Test basic extraction for a pair of links"""
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_extract_markdown_invalid_format_simple_link(self):
        """Test extraction doesn't return anything if invalid format (added !)"""
        matches = extract_markdown_links(
            "This is text with a link ![to boot dev](https://www.boot.dev)"
    )
        self.assertListEqual([], matches)  
        
    def test_extract_markdown_invalid_format_simple_url(self):
        """Test extraction doesn't return anything if invalid format - missing ("""
        matches = extract_markdown_links(
            "This is text with a link [to boot dev]https://www.boot.dev)"
    )
        self.assertListEqual([], matches)  
    
    def test_extract_markdown_links_invalid_format_pair(self):
        """Test extraction doesn't return anything if invalid format for one item (added !)"""
        matches = extract_markdown_links(
            "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
        self.assertListEqual([("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
        
    def test_extract_markdown_links_empty_string(self):
        """Test extraction for an empty string input"""
        matches = extract_markdown_links(
            ""
    )
        self.assertListEqual([], matches)
        
if __name__ == "__main__":
    unittest.main()