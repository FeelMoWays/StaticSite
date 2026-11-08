
import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(
            tag="img",
            props={"src": "image.png"}
        )

        self.assertEqual(
            node.props_to_html(),
            ' src="image.png"'
        )

    def test_to_html_raises_not_implemented_error(self):
        node = HTMLNode(tag="p", value="Hello")

        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
