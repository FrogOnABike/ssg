from htmlnode import LeafNode,ParentNode,HTMLNode
from textnode import TextNode,TextType
from block import Block,BlockType
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

def split_nodes_link(old_nodes):
    return_nodes = []
    for node in old_nodes:
        if re.search(r"(?<!!)(\[.*?\))",node.text) is None:
            return_nodes.append(node)
        else:
            node_split = re.split(r"(?<!!)(\[.*?\))",node.text)
            for i,txt in enumerate(node_split):
                if i % 2 ==0:
                    if len(txt) > 0:
                        return_nodes.append(TextNode(txt,TextType.TEXT))
                    next
                else:
                    temp = extract_markdown_links(txt)
                    return_nodes.append(TextNode(temp[0][0],TextType.LINK,temp[0][1]))
    return return_nodes

def split_nodes_image(old_nodes):
    return_nodes = []
    for node in old_nodes:
        if re.search(r"!(\[.*?\))",node.text) is None:
            return_nodes.append(node)
        else:
            node_split = re.split(r"!(\[.*?\))",node.text)
            for i,txt in enumerate(node_split):
                if i % 2 ==0:
                    if len(txt) > 0:
                        return_nodes.append(TextNode(txt,TextType.TEXT))
                    next
                else:
                    temp = extract_markdown_links(txt)
                    return_nodes.append(TextNode(temp[0][0],TextType.IMAGE,temp[0][1]))
    return return_nodes
        
    # print(re.search(r"(\[.*?\))",old_nodes.text))
    # node_split = re.split(r"(\[.*?\))",old_nodes.text)
    
def text_to_textnodes(text):
    master_nodes = [TextNode(text,TextType.TEXT)]
    
    master_nodes = split_nodes_delimiter(master_nodes,"**",TextType.BOLD)
    master_nodes = split_nodes_delimiter(master_nodes,"_",TextType.ITALIC)
    master_nodes = split_nodes_delimiter(master_nodes,"`",TextType.CODE)
    master_nodes = split_nodes_link(master_nodes)
    master_nodes = split_nodes_image(master_nodes)
    
    return master_nodes

def markdown_to_blocks(markdown):
    return_blocks = []
    split_blocks = markdown.split("\n\n")
    cleaned_blocks = [remove_newline_whitespace(block).strip() for block in split_blocks]
    return cleaned_blocks

def remove_newline_whitespace(text):
    """
    Removes whitespace between a newline character and the following character.

    Args:
        text: The input string.

    Returns:
        The modified string with the whitespace removed.
    """
    pattern = r"\n\s*([^\s])"
    return re.sub(pattern, r"\n\1", text)

def block_to_block_type(text):
    
    # print(f"Input text: {text}")
    
    if re.search("^(- )",text) is not None:
        # print(f"Found text(regex): {text}")
        # print(f"This is a {BlockType.UNORDERED_LIST.value} block")
        return BlockType.UNORDERED_LIST
    
    if re.search("^(\n|\t|\r)?\d+\. ",text,re.MULTILINE) is not None:
        # print(f"Found text(regex): {text}")
        # print(f"This is a {BlockType.ORDERED_LIST.value} block")
        return BlockType.ORDERED_LIST
    
    if re.search("^>( )?",text,re.MULTILINE) is not None:
        print(f"Found text(regex): {text}")
        print(f"This is a {BlockType.QUOTE.value} block")
        return BlockType.QUOTE
    
    if re.search("^`{3}",text,re.MULTILINE) is not None:
        # print(f"Found text(regex): {text}")
        # print(f"This is a {BlockType.CODE.value} block")
        return BlockType.CODE

    if re.search("^\#{1,6}\s*([^\#]*)\s*(\#{1,6})?$",text,re.MULTILINE) is not None:
        # print(f"Found text(regex): {text}")
        # print(f"This is a {BlockType.HEADING.value} block")
        return BlockType.HEADING
    
    else:
        print(f"This is a {BlockType.PARAGRAPH.value} block")
        return BlockType.PARAGRAPH
    
    # if text.startswith(">"):
    #     print(f"This is a {BlockType.QUOTE.value} block")
    #     return BlockType.QUOTE


