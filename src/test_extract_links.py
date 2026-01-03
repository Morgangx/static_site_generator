import unittest
from extract_links import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_extract_images(self) -> None:
        cases: list[tuple[str, list[tuple[str, str]]]] = [
            ("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
             [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
             ),
            ("This is a text with a ![dog](https://i.imgur.com/wqK8Ifr.jpeg)",
              [("dog","https://i.imgur.com/wqK8Ifr.jpeg")]),
        ]
        for (text, expected) in cases:
            result: list[tuple[str, str]] = extract_markdown_images(text)
            self.assertEqual(result, expected)


    def test_extract_links(self) -> None:
        cases: list[tuple[str, list[tuple[str, str]]]] = [
            ("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
             [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
             ),
            ("This is a text with a [to google](https://google.com) link.",
            [("to google", "https://google.com")]
            )
        ]

        for (text, expected) in cases:
            result: list[tuple[str, str]] = extract_markdown_links(text)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()