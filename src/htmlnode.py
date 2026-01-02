from __future__ import annotations
from abc import abstractmethod

class HTMLNode():
    def __init__(self, tag: str | None = None,
                    value: str | None = None,
                    children: list[HTMLNode] | None = None,
                    props: dict[str, str] | None = None
                 ) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[HTMLNode] | None = children
        self.props: dict[str, str] | None = props
    
    def __repr__(self) -> str:
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren:{self.children}\nprops:{self.props}"

    @abstractmethod
    def to_html(self) -> str:
        raise NotImplementedError("Not implemented yet")
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        html_list: list[str] = []
        for prop in self.props:
            html_list.append(f'{prop}="{self.props[prop]}"')
        return " " + " ".join(html_list)
    

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None , value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, children= None, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("No value provided")
        if not self.tag:
            return self.value
        
        props_str: str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self,
                    tag: str,
                    children: list[HTMLNode],
                    props: dict[str, str] | None = None
                ) -> None:
        super().__init__(tag, children=children, props=props)
    
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("No tag specified")
        if not self.children:
            raise ValueError("Missing children")
        
        inner: str = ""
        for child in self.children:
            inner += child.to_html()

        return f"<{self.tag}>{inner}</{self.tag}>"
    