import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_all_types(self) -> None:
        text = 'This is **text** with an _italic_ word and a `code block`' \
        ' and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        expected: list[TextNode] = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(expected, nodes)
    
    def test_all_inline_types(self) -> None:
        text = 'This is **text** with an _italic_ word and a `code block` and another _italic _**word.**' 
        expected: list[TextNode] = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and another ", TextType.TEXT),
            TextNode("italic ", TextType.ITALIC),
            TextNode("word.", TextType.BOLD),
        ]
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(expected, nodes)
    
    def test_bold_link(self) -> None:
        text = 'Plain text and **a [bold link](https://boot.dev) **' 
        expected: list[TextNode] = [
            TextNode("Plain text and ", TextType.TEXT),
            TextNode("a [bold link](https://boot.dev) ", TextType.BOLD),
        ]
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(expected, nodes)

    def test_italic_image(self) -> None:
        text = 'Plain text and _a ![italic obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) _' 
        expected: list[TextNode] = [
            TextNode("Plain text and ", TextType.TEXT),
            TextNode("a ![italic obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) ", TextType.ITALIC),
        ]
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(expected, nodes)

    def test_only_links(self) -> None:
        text = '[link](https://boot.dev)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)'
        expected: list[TextNode] = [
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(expected, nodes)
          

if __name__ == "__main__":
		unittest.main()