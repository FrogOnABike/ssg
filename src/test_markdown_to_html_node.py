import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from convertors import markdown_to_html_node

class TestTextNode(unittest.TestCase):   
    def test_paragraphs(self):
        """Test converting basic Markdown with just paragraphs and inline formating"""
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        """Test converting code block Markdown inline formating that shouldn't be touched!"""

        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        """Test converting code block Markdown inline formating that shouldn't be touched!"""

        md = """
> To be or not to be?
> That is a great question!
> Now can I just keep typing?
> How does this paste out????
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>To be or not to be?\n That is a great question!\n Now can I just keep typing?\n How does this paste out????</blockquote></div>",
        )

    def test_headerblock(self):
        """Test converting header block Markdown, and ensuring gets the right label for level"""

        md = """
# Heading

## Another heading

### Yet another!

#### Keep em coming!

##### Almost there

###### Blimey finally
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><h2>Another heading</h2><h3>Yet another!</h3><h4>Keep em coming!</h4><h5>Almost there</h5><h6>Blimey finally</h6></div>",
        )
        
    def test_unorderedlistblock(self):
        """Test converting an unordered list block Markdown"""

        md = """
- a list
- of random
- crap
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>a list</li><li>of random</li><li>crap</li></ul></div>",
        )
        
    def test_orderedlistblock(self):
        """Test converting an ordered list block Markdown"""

        md = """
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
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>A </li><li>nicely </li><li>ordered</li><li>list</li><li>of</li><li>items</li><li>with</li><li>lots</li><li>of</li><li>elements</li></ol></div>",
        )
if __name__ == "__main__":
    unittest.main()