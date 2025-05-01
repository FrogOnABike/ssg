from enum import Enum

class TextType(Enum):
    TEXT= "normal text"
    BOLD = "bold text"
    ITALIC = "italix text"
    CODE = "code text"
    LINK = "link text"
    IMAGE = "image text"
    DUMMY = "DUMMY TEST TYPE"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other_node):
        if (self.text == other_node.text) and (self.text_type.value == other_node.text_type.value) and (self.url == other_node.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

    