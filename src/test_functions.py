import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import *

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
    
    # **** Tests for split_nodes_delimiter ****
    
    def test_basic_text(self):
        """
        Tests a basic text node conversion, with no Markdown
        """
        node = TextNode("This is just a text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text,"This is just a text node")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        
    def test_code_text(self):
        """
        Tests a code text node conversion
        """
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text,"This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text," word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    
    def test_bold_text(self):
        """
        Tests a bold text node conversion
        """
        node = TextNode("This is text with some **bold text** included", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text,"This is text with some ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"bold text")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text," included")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    
    def test_italic_text_1(self):
        """
        Tests an itaic text node conversion using * delimiter
        """
        node = TextNode("This is text with some *italic text* included", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text,"This is text with some ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"italic text")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text," included")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_italic_text_2(self):
        """
        Tests an itaic text node conversion using _ delimiter
        """
        node = TextNode("This is text with some _italic text_ included", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text,"This is text with some ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"italic text")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text," included")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        
    def test_multiple_code_text(self):
        """
        Tests a code text node conversion with 2 code blocks.
        """
        node = TextNode("This is another text with a `code block` and another `code block secion!` after it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text,"This is another text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text," and another ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text,"code block secion!")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)
        self.assertEqual(new_nodes[4].text," after it")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
        
    def test_multiple_input_nodes(self):
        """
        Tests converting a list of TextNodes (Code + Text)
        """
        nodes = [TextNode("This is text with a `code block` word", TextType.TEXT),TextNode("This is just a text node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text,"This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text," word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text,"This is just a text node")
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)
    
    def test_multiple_input_nodes2(self):
        """
        Tests converting a list of TextNodes (Code + Bold) - Should only convert the code ones.
        """
        nodes = [TextNode("This is text with a `code block` word", TextType.TEXT),TextNode("This a **bold text** node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text,"This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text," word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text,"This a **bold text** node")
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)   
    
    def test_multiple_input_nodes3(self):
        """
        Tests converting a list of TextNodes (Code + Bold) - Should only convert the bold ones.
        """
        nodes = [TextNode("This is text with a `code block` word", TextType.TEXT),TextNode("This a **bold text** node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text,"This is text with a `code block` word")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text,"This a ")
        self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text,"bold text")
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[3].text," node")
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)

    def test_non_text_node_unchanged(self):
        """Test that non-TEXT nodes pass through unchanged"""
        node = TextNode("**already bold**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "**already bold**")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)

    def test_empty_string(self):
        """Test handling of empty strings"""
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    
    def test_delimiter_at_beginning(self):
        """Test delimiters at the beginning"""
        node = TextNode("`code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text, " text")
            
    def test_consecutive_delimiters(self):
        """Test handling of consecutive delimiters"""
        node = TextNode("Here's some `code` `more code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "Here's some ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "more code")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)
        self.assertEqual(new_nodes[4].text, " text")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_invalid_markdown_format(self):
        """
        Tests expected exception raised if invalid Markdown passed in
        """
        with self.assertRaises(Exception):
            node = TextNode("This is an invalid `code markdown node", TextType.TEXT)
            new_nodes = split_nodes_delimiter(node, "`", TextType.CODE)
            
    # *** Tests for test_extract_markdown_images ***
    
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
        
        
    # *** Tests for test_extract_markdown_links ***
    
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