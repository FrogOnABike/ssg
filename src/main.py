from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from convertors import *
from sitegen import *
from shutil import rmtree
import mistune

def main():
    
    rmtree("public")
    copy_content("static","public")
    generate_page("content/index.md","template.html","public/index.html")

if __name__ == "__main__":
    main()