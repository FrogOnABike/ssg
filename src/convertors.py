from htmlnode import LeafNode,ParentNode,HTMLNode
from textnode import TextNode,TextType
from block import Block,BlockType
import enum
import re

def text_node_to_html_node(text_node):
    # Create a LeafNode from a TextNode based on TextType
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
    # Takes a list of TEXT TextNodes and returns an updates list of TextNodes with correct TextType
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
    # Extract image text and URL
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    # Extract link text and URL
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def split_nodes_link(old_nodes):
    # Takes a list of TEXT TextNodes and returns an updates list of TextNodes with correct TextType, Value and URL for links
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
    # Takes a list of TEXT TextNodes and returns an updates list of TextNodes with correct TextType, Value and URL for images
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
    # Converts raw Markdown and retruns a list of TextNodes for inline items (Bold, Italic, Code, Links and Images)
    master_nodes = [TextNode(text,TextType.TEXT)]
    
    master_nodes = split_nodes_delimiter(master_nodes,"**",TextType.BOLD)
    master_nodes = split_nodes_delimiter(master_nodes,"_",TextType.ITALIC)
    master_nodes = split_nodes_delimiter(master_nodes,"`",TextType.CODE)
    master_nodes = split_nodes_link(master_nodes)
    master_nodes = split_nodes_image(master_nodes)
    
    return master_nodes

def markdown_to_blocks(markdown):
    # Splits Markdown into blocks, which can then be checked via block_to_block_type - Returns a list of strings, so need to iterate over that
    return_blocks = []
    split_blocks = markdown.split("\n\n")
    print(f"Split blocks before removing blanks: {split_blocks}")
    for i,txt in enumerate(split_blocks):
        if txt == "":
            del split_blocks[i]
    print(f"Split blocks after blanks: {split_blocks}")
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
    if re.sub(pattern, r"\n\1", text) is None:
        return
    return re.sub(pattern, r"\n\1", text)

def block_to_block_type(text):
    # Returns a BlockType for Markdown text
    if re.search("^(- )",text) is not None:
        return BlockType.UNORDERED_LIST
    
    if re.search("^(\n|\t|\r)?\d+\. ",text,re.MULTILINE) is not None:
        return BlockType.ORDERED_LIST
    
    if re.search("^>( )?",text,re.MULTILINE) is not None:
        return BlockType.QUOTE
    
    if re.search("^`{3}",text,re.MULTILINE) is not None:
        return BlockType.CODE

    if re.search("^\#{1,6}\s*([^\#]*)\s*(\#{1,6})?$",text,re.MULTILINE) is not None:
        return BlockType.HEADING
    
    else:
        return BlockType.PARAGRAPH
    
    # if text.startswith(">"):
    #     print(f"This is a {BlockType.QUOTE.value} block")
    #     return BlockType.QUOTE


def markdown_to_html_node(markdown):
    master_nodes=[]
    blocks = markdown_to_blocks(markdown)
    # print(f"Converted blocks: {blocks}")
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                block_tn = []
                child_nodes = []
                block_tn = text_to_textnodes(block.replace("\n"," "))
                for kid in block_tn:
                    child_nodes.append(text_node_to_html_node(kid))
                master_nodes.append(ParentNode("p",child_nodes))
            case BlockType.CODE:
                # print(f"Block: {block}")
                text = block.strip("```").lstrip()
                # print(f"Text after removing ```:{text}")
                code_tn = TextNode(text,TextType.CODE)
                # print(f"Code TN: {code_tn}")
                child_node = text_node_to_html_node(code_tn)
                # print(f"Child Node:{child_node}")
                master_nodes.append(ParentNode("pre",[child_node]))
            case BlockType.QUOTE:
                text = block.replace(">","")
                # text = re.sub("^> ?","")
                quote_ln = LeafNode("p",text)
                master_nodes.append(ParentNode("blockquote",[quote_ln]))
            case BlockType.HEADING:
                i = block.count("#",0,6)
                print(f"Heading level:{i}")
                text = block.lstrip("#").strip()
                print(f"Header text:{text}")
                master_nodes.append(LeafNode(f"h{i}",text))
            case BlockType.UNORDERED_LIST:
                child_nodes = []
                items = block.splitlines()
                print(f"Split lines:{items}")
                for i in items:
                    text = i.lstrip("- ")
                    child_nodes.append(LeafNode("li",text))
                master_nodes.append(ParentNode("ul",child_nodes))
            case BlockType.ORDERED_LIST:
                child_nodes = []
                items = block.splitlines()
                print(f"Split lines:{items}")
                for i in items:
                    text = re.sub("(\d*\. )","",i)
                    child_nodes.append(LeafNode("li",text))
                master_nodes.append(ParentNode("ol",child_nodes))
                       
    return ParentNode("div",master_nodes)
                                                