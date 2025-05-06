from enum import Enum

class BlockType(Enum):
    PARAGRAPH= "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

class Block:
    def __init__(self,text,block_type):
        self.text = text
        self.block_type = block_type
    
    def __repr__(self):
        return f"Block({self.text}, {self.block_type.value})"
    

    