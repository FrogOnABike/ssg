from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from convertors import text_node_to_html_node,split_nodes_delimiter

def main():
    # test_textnode = TextNode("This is some test text",TextType.ANCHOR,"https://www.boot.dev")
    # print(test_textnode)

    # test_htmlnode = HTMLNode("a","This is a test HTML value",None,{"href": "https://www.google.com","target": "_blank",})
    # test_htmlnode2 = HTMLNode("p","This is a test HTML para",[test_htmlnode])
    # print(test_htmlnode)
    # print(test_htmlnode.props_to_html())
    # print(test_htmlnode2)
    # print(test_htmlnode2.props_to_html())
    # # test_htmlnode.to_html()
    # print(LeafNode("p", "This is a paragraph of text.").to_html())
    # print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())

#     node = ParentNode(
#     "div",
#     [
#         ParentNode("span", [LeafNode(None, "nested")], {"class": "myspan"}),
#     ],
#     {"id": "outer"}
# )
    
#     complex_node = ParentNode(
#         "body",
#         [
#             ParentNode(
#                 "header",
#                 [
#                     ParentNode("nav", [
#                         ParentNode("ul", [
#                             LeafNode("li", "Home"),
#                             LeafNode("li", "Products"),
#                             ParentNode("li", [
#                                 LeafNode("a", "Contact Us", {"href": "/contact"})
#                             ]),
#                         ]),
#                     ]),
#                 ],
#                 {"id": "top-header"}
#             ),
#             ParentNode(
#                 "main",
#                 [
#             ParentNode("section", [
#                 ParentNode("h2", [LeafNode("span", "Section Title", {"class": "title-span"})]),
#                     LeafNode("p", "Section introduction."),
#                     ParentNode("div", [
#                         LeafNode("div", "Block 1", {"class": "block"}),
#                         LeafNode("div", "Block 2", {"class": "block"}),
#                     ], {"class": "blocks-container"})
#                 ]),
#                 ParentNode("footer", [
#                     LeafNode("p", "© 2024 My Website"),
#                 ])
#             ],
#             {"class": "main-content"}
#         ),
#     ],

# )
    

#     complex_node2 = ParentNode(
#     "body",
#     [
#         ParentNode(
#             "header",
#             [
#                 ParentNode("nav", [
#                     ParentNode("ul", [
#                         LeafNode("li", "Home"),
#                         LeafNode("li", "Products"),
#                         ParentNode("li", [
#                             LeafNode("a", "Contact Us", {"href": "/contact"})
#                         ]),
#                     ]),
#                 ]),
#             ],
#             {"id": "top-header"}
#         ),
#         ParentNode(
#             "main",
#             [
#                 ParentNode("section", [
#                     ParentNode("h2", [LeafNode("span", "Section Title", {"class": "title-span"})]),
#                     LeafNode("p", "Section introduction."),
#                     ParentNode("div", [
#                         LeafNode("div", "Block 1", {"class": "block"}),
#                         LeafNode("div", "Block 2", {"class": "block"}),
#                     ], {"class": "blocks-container"})
#                 ]),
#                 ParentNode("footer", [
#                     LeafNode("p", "© 2024 My Website"),
#                 ]),
#                 ParentNode("orphan",[])
#             ],
#             {"class": "main-content"}
#         ),
#     ],
#     {"class": "foo", "id": "bar"},
# )
    # print(f"Regular node to html: {node.to_html()}")
    # print(f"Complex node structure: {complex_node}")
    # print(f"Complex node to html: {complex_node.to_html()}")
    # print(f"Complex node2 structure: {complex_node2}")
    # print(f"Complex node2 to html: {complex_node2.to_html()}")
    
    # node = TextNode("This is an invalid node", TextType.DUMMY)
    # print(text_node_to_html_node(node))
    
    # nodes = [TextNode("This is text with a `code block` word", TextType.TEXT),TextNode("This is another text with a `code block` and another `code block secion!`", TextType.TEXT),TextNode("This is just a text node", TextType.TEXT)]
    node = TextNode("**already bold**", TextType.BOLD)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)
    
    for node in new_nodes:
        print(text_node_to_html_node(node))

if __name__ == "__main__":
    main()