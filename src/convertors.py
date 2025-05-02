from htmlnode import LeafNode,ParentNode,HTMLNode
from textnode import TextNode,TextType
import enum
import re

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            return LeafNode("a",text_node.text,{"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","",{"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Invalid or unsupported text node type")
            
            
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    for node in old_nodes:
        match node.text_type:
            case TextType.TEXT:
                if (node.text.count(delimiter)) % 2 != 0:
                    raise Exception("Not valid Markdown syntax")
                split_text = node.text.split(delimiter)
                for i,txt in enumerate(split_text):
                    if i % 2 ==0:
                        return_nodes.append(TextNode(txt, TextType.TEXT))
                    else:
                        return_nodes.append(TextNode(txt,text_type))
            case _:
                return_nodes.append(node)
    return return_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)