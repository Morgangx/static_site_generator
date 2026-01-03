from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes: list[TextNode]= []
        sections: list[str] = old_node.text.split(delimiter)
        if len(sections) % 2 == 0: 
            raise ValueError("Invalid inline markdown syntax.")
        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 != 0:
                split_nodes.append(TextNode(section, text_type))
            else:
                split_nodes.append(TextNode(section, TextType.TEXT)) 
        new_nodes.extend(split_nodes)

    return new_nodes
