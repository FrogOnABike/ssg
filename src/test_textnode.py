import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        node3 = TextNode("This is a test node", TextType.BOLD)
        node4 = TextNode("This is a TEXT node", TextType.TEXT)
        node5 = TextNode("This is a TEXT node", TextType.TEXT)
        node6 = TextNode("This is a URL node", TextType.LINK,url="www.boot.dev")
        node7 = TextNode("This is a URL node", TextType.LINK,url="www.boot.dev")
        self.assertEqual(node, node2)
        self.assertEqual(node4, node5)
        self.assertEqual(node6, node7)

    def test_not_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold test node", TextType.BOLD)
        node3 = TextNode("This is a TEXT test node", TextType.TEXT)
        node4 = TextNode("This is a TEXT test node", TextType.TEXT)
        node5 = TextNode("This is a bold text node", TextType.BOLD,url="None")
        node6 = TextNode("This is a URL node", TextType.LINK,url="www.boot.dev")
        node7 = TextNode("This is a different URL node", TextType.LINK,url="www.boot.dev")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node6,node7)
        self.assertNotEqual(node, node5)


if __name__ == "__main__":
    unittest.main()