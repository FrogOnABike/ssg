from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from convertors import *
import mistune

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
    
    # new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    # print(new_nodes)
    
    # for node in new_nodes:
    #     print(text_node_to_html_node(node))
    
        # ****TESTING VARS BELOW!****
    # Bold TextNode
    # node = TextNode("**already bold**", TextType.BOLD)
     
    # Code TextNode
    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
            
    # Text node containing links to test conversion
    # node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)   
    
    # Text node containing image links to test conversion
    node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)


    # ****Text string****
    text = "This is **bold text** with an _italic word_ and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    markdown = mistune.create_markdown(renderer='ast')
    
    # print(f"Image extractor: {extract_markdown_images(text)}")
    
    # print(f"Link extractor: {extract_markdown_links(text)}")
    # print(f"Output from mistune: {markdown(text)}")
    
    # print(f"split_nodes_link: {split_nodes_link([node])}")
    
    # print(f"split_nodes_image: {split_nodes_image([node])}")
    
    print(f"Text to TextNode output: {text_to_textnodes(text)}")








if __name__ == "__main__":
    main()