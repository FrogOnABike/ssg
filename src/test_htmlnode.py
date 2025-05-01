import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        test_htmlnode1 = HTMLNode("a","This is a test HTML value",None,{"href": "https://www.google.com","target": "_blank",})
        test_htmlnode2 = HTMLNode("p","This is a test HTML paragraph",[test_htmlnode1],{"href": "https://www.boot.dev","target": "_blank",})
        test_htmlnode3 = HTMLNode("h1","This is a test HTML header",[test_htmlnode2])

        expected_props1 = " href=\"https://www.google.com\" target=\"_blank\""
        expected_props2 = " href=\"https://www.boot.dev\" target=\"_blank\""
        expected_props3 = ""

        self.assertEqual(test_htmlnode1.props_to_html(), expected_props1)
        self.assertEqual(test_htmlnode2.props_to_html(), expected_props2)
        self.assertEqual(test_htmlnode3.props_to_html(), expected_props3)

    def test_leaf_to_html_p(self):
        node1 = LeafNode("p", "Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})  
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

        node3 = LeafNode("b", "Hello, world!")
        self.assertEqual(node3.to_html(), "<b>Hello, world!</b>")

        node4 = LeafNode(None, "Hello, world!")
        self.assertEqual(node4.to_html(), "Hello, world!")

        # node5 = LeafNode("b")
        # self.assertRaises(ValueError,node5.to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_with_props(self):
        child_node = LeafNode("a", "child",{"href": "https://www.google.com","target": "_blank",})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><a href=\"https://www.google.com\" target=\"_blank\">child</a></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",)

    def test_complex_nested_html_with_top_level_props(self):
        """
        Tests a more complex nested structure with multiple levels of nesting and various tags.
        """
        complex_node = ParentNode(
            "body",
            [
                ParentNode(
                    "header",
                    [
                        ParentNode("nav", [
                            ParentNode("ul", [
                                LeafNode("li", "Home"),
                                LeafNode("li", "Products"),
                                ParentNode("li", [
                                    LeafNode("a", "Contact Us", {"href": "/contact"})
                                ]),
                            ]),
                        ]),
                    ],
                    {"id": "top-header"}
                ),
                ParentNode(
                    "main",
                    [
                        ParentNode("section", [
                            ParentNode("h2", [LeafNode("span", "Section Title", {"class": "title-span"})]),
                            LeafNode("p", "Section introduction."),
                            ParentNode("div", [
                                LeafNode("div", "Block 1", {"class": "block"}),
                                LeafNode("div", "Block 2", {"class": "block"}),
                            ], {"class": "blocks-container"})
                        ]),
                        ParentNode("footer", [
                            LeafNode("p", "© 2024 My Website"),
                        ])
                    ],
                    {"class": "main-content"}
                ),
            ],
            {"id": "body"},
        )
        expected_html = ('<body id="body"><header id="top-header"><nav><ul><li>Home</li><li>Products</li><li><a href="/contact">Contact Us</a></li></ul></nav></header><main class="main-content"><section><h2><span class="title-span">Section Title</span></h2><p>Section introduction.</p><div class="blocks-container"><div class="block">Block 1</div><div class="block">Block 2</div></div></section><footer><p>© 2024 My Website</p></footer></main></body>')
        self.maxDiff = None
        self.assertEqual(complex_node.to_html(), expected_html)
        
    def test_parentnode_errors(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()  # children is None
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()  # children is empty
        with self.assertRaises(TypeError):
            ParentNode().to_html() #Can't be empty

    def test_leafnode_errors(self):
        with self.assertRaises(ValueError):
            LeafNode("p").to_html()  # value is None

if __name__ == "__main__":
    unittest.main()