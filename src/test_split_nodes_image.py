import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import split_nodes_image

basic_image_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",TextType.TEXT)
basic_image_node2 = TextNode("This is text with an ![image](https://i.imgur.com/zoo.png)",TextType.TEXT)
basic_image_no_text_node = TextNode("![image](https://i.imgur.com/zoo.png)",TextType.TEXT)

multi_image_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)
multi_image_node2 = TextNode("This is text with an ![image](https://i.imgur.com/zoo.png) and another ![second image](https://i.imgur.com/cat.png)",TextType.TEXT)
multi_image_no_text_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)

multi_link_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
multi_link_node2 = TextNode("This is text with a link [to bbc](https://www.bbc.com) and [to foobar](https://foo.bar)",TextType.TEXT)
multi_link_no_text_node = TextNode("[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)

basic_text_node = TextNode("This is just a text node",TextType.TEXT)
mixed_type_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link to boot.dev](https://boot.dev) website",TextType.TEXT)
mixed_type_node2 = TextNode("This is text with an ![image](https://i.imgur.com/zoo.png) and a [link to bbc](https://bbc.com) website",TextType.TEXT)

class TestTextNode(unittest.TestCase):   
                    
    # **** Tests for split_nodes_image ****
    
    def test_split_images_single(self):
        """Test extraction for an image links in a single TextNode"""
        new_nodes = split_nodes_image([basic_image_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
            
    def test_split_images_pair(self):
        """Test extraction for a pair of image links in a single TextNode"""
        new_nodes = split_nodes_image([multi_image_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_images_mixed(self):
        """Test extraction for a mixed image and link TextNode - Should only proces image one"""
        new_nodes = split_nodes_image([mixed_type_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a [link to boot.dev](https://boot.dev) website", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_images_multiple_input_nodes(self):
        """Test extraction for 2 image TextNodes"""
        # node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link to boot.dev](https://boot.dev)",TextType.TEXT)
        new_nodes = split_nodes_image([basic_image_node,basic_image_node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zoo.png"),
            ],
            new_nodes,
        )
    
    def test_split_images_multiple_input_pair_nodes(self):
        """Test extraction for 2 image TextNodes with multiple images"""
        new_nodes = split_nodes_image([multi_image_node,multi_image_node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zoo.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/cat.png"),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()