from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from convertors import *
from sitegen import copy_content
import mistune

def main():
    copy_content("static","public")

if __name__ == "__main__":
    main()