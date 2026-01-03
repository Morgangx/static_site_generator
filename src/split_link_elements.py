from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links
from typing import Callable

def split_nodes(
        old_nodes: list[TextNode], fun: Callable[[str], list[tuple[str, str]]], form_string: str, txt_type: TextType
    ) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        text: str = old_node.text
        extracted_links: list[tuple[str, str]] = fun(text)

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        if extracted_links == []:
            new_nodes.append(old_node)
            continue

        for (node_text, node_url) in extracted_links:
            formatted: str = form_string.format(node_text, node_url)
            sections: list[str] = text.split(formatted, maxsplit=1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(node_text, txt_type, node_url))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes(old_nodes, extract_markdown_images, "![{}]({})", TextType.IMAGE)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes(old_nodes, extract_markdown_links, "[{}]({})", TextType.LINK)
