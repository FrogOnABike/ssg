from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from convertors import *
from sitegen import *
from shutil import rmtree
import mistune
from sys import argv

def main():
    print(f"Argv:{argv}")
    if len(argv) == 1:
        basepath = "/"
    else:
        basepath = argv[1]

    copy_content("static","docs")
    # generate_page("content/index.md","template.html","public/index.html")
    generate_pages_recursive("content","template.html","docs",basepath)

if __name__ == "__main__":
    main()