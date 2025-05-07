from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from convertors import *
import mistune

def main():
    markdown = mistune.create_markdown(renderer='ast')
    # node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)
text = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
print(markdown_to_html_node(text))



if __name__ == "__main__":
    main()