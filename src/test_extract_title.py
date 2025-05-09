import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from sitegen import extract_title

heading_basic = "# BasicHeading"
heading_multi = "# Multi-word heading"
heading_mult2 = "# Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
invalid_heading = "## Not a top-level heading"
invalid_heading2 = "Just plain text"

class TestTextNode(unittest.TestCase):   
    
   def test_basic(self):
       """Text extraction for a single word header"""
       result = extract_title(heading_basic)
       self.assertEqual("BasicHeading",result)
   
   def test_multi1(self):
       """Text extraction for a multi word header"""
       result = extract_title(heading_multi)
       self.assertEqual("Multi-word heading",result)

   def test_multi2(self):
       """Text extraction for a much longer mulit word header"""
       result = extract_title(heading_mult2)
       self.assertEqual("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",result)
       
   def test_invalid1(self):
       """Text exception raised for L2 header"""
       with self.assertRaises(Exception):
        extract_title(invalid_heading)
       
   def test_invalid2(self):
       """Text exception raised for plain text"""
       with self.assertRaises(Exception):
           extract_title(invalid_heading2)
       
if __name__ == "__main__":
    unittest.main()