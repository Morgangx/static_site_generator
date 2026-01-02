import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node4 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node5 = TextNode("This is another text node", TextType.ITALIC, "https://boot.dev")
        node6 = TextNode("This is another text node", TextType.ITALIC, "https://boot.dev")
        
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node3, node6)
    

if __name__ == "__main__":
    unittest.main()