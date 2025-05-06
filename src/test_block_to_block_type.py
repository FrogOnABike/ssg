import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from block import Block,BlockType
from convertors import block_to_block_type

valid_heading1 = """# 1x Heading"""
valid_heading2 = """## 2x Heading"""
valid_heading3 = """### 3x Heading"""
valid_heading4 = """#### 4x Heading"""
valid_heading5 = """##### 5x Heading"""
valid_heading6 = """###### 6x Heading"""
invalid_heading7 = """####### 7x Invalid Heading"""

paragraph = """This is just some paragraph text"""

code_block = """```
This is a code test block
````"""

quote_block = """> To be or not to be innit mate?"""
quote_block2 = """>This ain't got trailing space after the opening"""

unordered_list = """- a list
- of random
- crap"""

ordered_list = """1. A 
2. nicely 
3. ordered
4. list"""


class TestTextNode(unittest.TestCase):   
    def test_heading1(self):
        """Tests for correct return from a single # heading"""
        self.assertEqual(block_to_block_type(valid_heading1),BlockType.HEADING)

    def test_heading2(self):
        """Tests for correct return from a 2# heading"""
        self.assertEqual(block_to_block_type(valid_heading2),BlockType.HEADING)
        
    def test_heading3(self):
        """Tests for correct return from a 3# heading"""
        self.assertEqual(block_to_block_type(valid_heading3),BlockType.HEADING)

    def test_heading4(self):
        """Tests for correct return from a 4# heading"""
        self.assertEqual(block_to_block_type(valid_heading4),BlockType.HEADING)
        
    def test_heading5(self):
        """Tests for correct return from a 5# heading"""
        self.assertEqual(block_to_block_type(valid_heading5),BlockType.HEADING)

    def test_heading6(self):
        """Tests for correct return from a 6# heading"""
        self.assertEqual(block_to_block_type(valid_heading6),BlockType.HEADING)
        
    def test_heading7(self):
        """Tests for correct return from a 7# heading (should be a paragraph type!)"""
        self.assertEqual(block_to_block_type(invalid_heading7),BlockType.PARAGRAPH)
        
    def test_paragraph(self):
        """Tests for correct return from a plain boring paragraph!"""
        self.assertEqual(block_to_block_type(paragraph),BlockType.PARAGRAPH)
        
    def test_code(self):
        """Tests for correct return from a code block"""
        self.assertEqual(block_to_block_type(code_block),BlockType.CODE)
    
    def test_quote(self):
        """Tests for correct return from a quote block"""
        self.assertEqual(block_to_block_type(quote_block),BlockType.QUOTE)
        
    def test_quote2(self):
        """Tests for correct return from a quote block with some whitespace"""
        self.assertEqual(block_to_block_type(quote_block2),BlockType.QUOTE)
        
    def test_unordered_list(self):
        """Tests for correct return from an unordered list block"""
        self.assertEqual(block_to_block_type(unordered_list),BlockType.UNORDERED_LIST)
        
    def test_unordered_list(self):
        """Tests for correct return from a list block"""
        self.assertEqual(block_to_block_type(ordered_list),BlockType.ORDERED_LIST)
        
if __name__ == "__main__":
    unittest.main()