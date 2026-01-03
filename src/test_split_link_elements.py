import unittest
from textnode import TextType, TextNode
from split_link_elements import split_nodes_image, split_nodes_link

class TestTextNode(unittest.TestCase):
    def test_split_images(self) -> None:
        cases: list[tuple[TextNode, list[TextNode]]]=[
            (TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
                " and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT),
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ]),
            (TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and plain text.",
            TextType.TEXT),
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and plain text.", TextType.TEXT),
            ]),
            (TextNode(
                "This is a plain text.",TextType.TEXT),
            [
                TextNode("This is a plain text.", TextType.TEXT),
            ]),
            (TextNode(
                "![image](https://i.imgur.com/zjjcJKZ.png).",TextType.BOLD),
            [
                TextNode("![image](https://i.imgur.com/zjjcJKZ.png).",TextType.BOLD),
            ]),
        ]
        for input_node, expected_nodes in cases:
            actual: list[TextNode] = split_nodes_image([input_node])
            self.assertListEqual(expected_nodes, actual)
    
    def test_split_links(self) -> None:
        cases: list[tuple[TextNode, list[TextNode]]]=[
            (TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT),
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ]),
            (TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT),
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ]),
            (TextNode(
            "[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT),
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ]),

        ]
        for input_node, expected_nodes in cases:
            actual: list[TextNode] = split_nodes_link([input_node])
            self.assertListEqual(expected_nodes, actual)