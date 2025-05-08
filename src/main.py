from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from convertors import *
import mistune

def main():
    markdown = mistune.create_markdown(renderer='ast')
    # node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)
text = """
When referencing, [-1] is last element only and returns a str
[-1:] will return a list!

# Heading

## Another heading

### Yet another!

#### Keep em coming!

##### Almost there

###### Blimey finally

####### You mean I can't add more?

```
code block, Im used to these!
```

>To be or not to be?
>That is a great question!
>Now can I just keep typing?
>How does this paste out????



- a list
- of random
- crap

1. A 
2. nicely 
3. ordered
4. list
5. of
6. items
7. with
8. lots
9. of
10. elements

Just plan text, maybe lets add some _italic_ and **bold text** in to ensure those work!

How about some [links](http://www.bbc.com)?

"""
print(markdown_to_html_node(text))
html = markdown_to_html_node(text)
print(html.to_html())



if __name__ == "__main__":
    main()