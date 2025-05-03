import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import split_nodes_link

basic_link_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)",TextType.TEXT)
basic_link_node2 = TextNode("This is another text with a link [to bbc](https://www.bbc.com)",TextType.TEXT)
basic_link_no_text_node = TextNode("[to boot dev](https://www.boot.dev)",TextType.TEXT)

multi_link_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
multi_link_node2 = TextNode("This is text with a link [to bbc](https://www.bbc.com) and [to foobar](https://foo.bar)",TextType.TEXT)
multi_link_no_text_node = TextNode("[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)

multi_image_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)
multi_image_node2 = TextNode("This is text with an ![image](https://i.imgur.com/zoo.png) and another ![second image](https://i.imgur.com/cat.png)",TextType.TEXT)
multi_image_no_text_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)

basic_text_node = TextNode("This is just a text node",TextType.TEXT)
mixed_type_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link to boot.dev](https://boot.dev) website",TextType.TEXT)
mixed_type_node2 = TextNode("This is text with an ![image](https://i.imgur.com/zoo.png) and a [link to bbc](https://bbc.com) website",TextType.TEXT)


class TestTextNode(unittest.TestCase):
                    
    # **** Tests for split_nodes_link ****
    
    def test_split_link_single(self):
        """Test extraction for simple link in a single TextNode"""
        new_nodes = split_nodes_link([basic_link_node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_link_pair(self):
        """Test extraction for a pair of links in a single TextNode"""
        new_nodes = split_nodes_link([multi_link_node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_split_link_mixed(self):
        """Test extraction for a mixed image and link TextNode - Should only proces link one"""
        new_nodes = split_nodes_link([mixed_type_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ", TextType.TEXT),
                TextNode("link to boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" website", TextType.TEXT),
            ],
            new_nodes,
        )
       
    def test_split_link_multiple_input_nodes(self):
        """Test extraction for 2 input nodes containing a single link"""
        new_nodes = split_nodes_link([basic_link_node,basic_link_node2])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode("This is another text with a link ", TextType.TEXT),
                TextNode("to bbc", TextType.LINK, "https://www.bbc.com"),
            ],
            new_nodes,
        )

    def test_split_link_multiple_input_nodes_2_links(self):
        """Test extraction for 2 input nodes containing multiple links"""
        new_nodes = split_nodes_link([multi_link_node,multi_link_node2])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to bbc", TextType.LINK, "https://www.bbc.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to foobar", TextType.LINK, "https://foo.bar"),
            ],
            new_nodes,
        )

    def test_split_link_all_text(self):
        """Test extraction for a TextNode without any link"""
        new_nodes = split_nodes_link([basic_text_node])
        self.assertListEqual(
            [
                TextNode("This is just a text node", TextType.TEXT),
            ],
            new_nodes,
        )     
        
    def test_no_text_link_single(self):
        """Test extraction for simple link, with no text, in a single TextNode"""
        new_nodes = split_nodes_link([basic_link_no_text_node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_no_text_link_pair(self):
        """Test extraction for a pair of links, with no text, in a single TextNode"""
        new_nodes = split_nodes_link([multi_link_no_text_node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )
        
    def test_split_multiple_link_mixed(self):
        """Test extraction for a pair of mixed image and link TextNode - Should only link in each one"""
        new_nodes = split_nodes_link([mixed_type_node,mixed_type_node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ", TextType.TEXT),
                TextNode("link to boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" website", TextType.TEXT),
                TextNode("This is text with an ![image](https://i.imgur.com/zoo.png) and a ", TextType.TEXT),
                TextNode("link to bbc", TextType.LINK, "https://bbc.com"),
                TextNode(" website", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_mixed_basic_text(self):
        """Test extraction for a pair of mixed image and link TextNode - Should only link in each one"""
        new_nodes = split_nodes_link([mixed_type_node,basic_text_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a ", TextType.TEXT),
                TextNode("link to boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" website", TextType.TEXT),
                TextNode("This is just a text node", TextType.TEXT),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()