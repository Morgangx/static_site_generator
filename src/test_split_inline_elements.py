import unittest
from split_inline_elements import split_nodes_delimiter
from textnode import TextType, TextNode

# It's generally better to define delimiters within the test if they're specific to the test

class TestTextNode(unittest.TestCase):
    def test_code_block_split(self) -> None:
            node = TextNode("This is text with a `code block` word", TextType.TEXT)
            expected: list[TextNode] = [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word", TextType.TEXT),
            ]
            # Notice we're passing [node] because split_nodes_delimiter expects a list
            result: list[TextNode] = split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertListEqual(result, expected)

    def test_bold_split(self) -> None:
            node = TextNode("Normal text **bold part** rest.", TextType.TEXT)
            expected: list[TextNode] = [
                    TextNode("Normal text ", TextType.TEXT),
                    TextNode("bold part", TextType.BOLD),
                    TextNode(" rest.", TextType.TEXT),
            ]
            result: list[TextNode] = split_nodes_delimiter([node], "**", TextType.BOLD)
            self.assertListEqual(result, expected)

    def test_multiple_bold_splits(self) -> None:
            node = TextNode("**Bold text** and **another bold text**.", TextType.TEXT)
            expected: list[TextNode] = [
                    TextNode("Bold text", TextType.BOLD),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("another bold text", TextType.BOLD),
                    TextNode(".", TextType.TEXT),
            ]
            result: list[TextNode] = split_nodes_delimiter([node], "**", TextType.BOLD)
            self.assertListEqual(result, expected)

    def test_no_split_if_different_text_type(self) -> None:
            node = TextNode("Bold text with a _italic__ part.", TextType.BOLD)
            expected: list[TextNode] = [
                    TextNode("Bold text with a _italic__ part.", TextType.BOLD),
            ]
            # The delimiter is for italic, but the node is already bold, so it shouldn't split
            result: list[TextNode] = split_nodes_delimiter([node], "_", TextType.ITALIC)
            self.assertListEqual(result, expected)

    def test_split_nodes_delimiter_errors(self) -> None:
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(ValueError) as cm:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(cm.exception), "Invalid inline markdown syntax.")

    def test_split_nodes_delimiter_errors2(self) -> None:
        node = TextNode("This is text with a `code block word``", TextType.TEXT)
        with self.assertRaises(ValueError) as cm:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(cm.exception), "Invalid inline markdown syntax.")


if __name__ == "__main__":
		unittest.main()