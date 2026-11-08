from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None,props=None) -> None:
        self.tag = tag
        self.value = value
        self.props = props or {}

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        props = self.props_to_html()
        if props:
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"