import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self) -> None:
        node: HTMLNode = HTMLNode("a", "paragrapth", None, {"href": "https://google.com", "target": "_blank"})
        html: str = node.props_to_html()
        node2: HTMLNode = HTMLNode("a", "paragrapth", None, {"href": "https://google.com", "target": "_blank"})
        html2: str = node2.props_to_html()
        node3: HTMLNode = HTMLNode("a", "paragrapth", None, {"href": "https://google.com"})
        html3: str = node3.props_to_html()
        node4: HTMLNode = HTMLNode("b", "paragrapth", None, None)
        html4: str = node4.props_to_html()

        self.assertNotEqual(node, node2)
        self.assertEqual(html, html2)
        self.assertNotEqual(html2, html3)
        self.assertNotEqual(node3, node4)
        self.assertEqual(html4, "")

    def test_leaf_to_html_p(self) -> None:
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "google", {"href": "https://google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://google.com">google</a>')
        node3 = LeafNode("b", "This is bold text.")
        self.assertEqual(node3.to_html(), "<b>This is bold text.</b>")
        node4 = LeafNode(None, "Plain text...")
        self.assertEqual(node4.to_html(), "Plain text...")

    def test_to_html_with_children(self) -> None:
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self) -> None:
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self) -> None:
        child_node1 = LeafNode("b", "Bold text")
        child_node2 = LeafNode(None, "Normal text 1")
        child_node3 = LeafNode("i", "italic text")
        child_node4 = LeafNode(None, "Normal text 2")
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text 1<i>italic text</i>Normal text 2</p>"
        )

    def test_to_html_with_no_children(self) -> None:
        parent_node = ParentNode("a", [])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(str(cm.exception), "Missing children")

    def test_to_html_with_no_tag(self) -> None:
        child_node1 = LeafNode("b", "Bold text")  
        parent_node = ParentNode("", [child_node1])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        self.assertEqual(str(cm.exception), "No tag specified")

if __name__ == "__main__":
    unittest.main()