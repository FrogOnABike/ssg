class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_str=""
        for k in self.props:
            v = self.props[k]
            props_str += f' {k}="{v}"'
        return props_str
    
    def __repr__(self):
        return f"\nHTMLNode:\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Value is mandatory")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"\nLeaf Node:\nTag: {self.tag}\nValue: {self.value}\nProps: {self.props}"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag,children=children,props=props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("Object MUST have a tag!")
        if self.children == [] or self.children is None:
            raise ValueError("Children are required")
        html_str=""
        if self.children:
            for child in self.children:
                html_str += child.to_html()
                # print(f"HTML String: {html_str}")
        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"
    
    def __repr__(self):
        return f"\nParent Node:\nTag: {self.tag}\nChildren: {self.children}\nProps: {self.props}"