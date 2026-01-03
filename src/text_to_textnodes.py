from textnode import TextNode, TextType
from split_inline_elements import split_nodes_delimiter
from split_link_elements import split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes : list[TextNode] = [TextNode(text, TextType.TEXT)]
    if "**" in text:
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    if "_" in text:
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    if "`" in text:
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
