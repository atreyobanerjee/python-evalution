import unittest
from justify import justify_text

class TestJustifyText(unittest.TestCase):
    def test_default_text(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        width = 20
        expected_output = [
            "This   is  a  sample",
            "text      but      a",
            "complicated  problem",
            "to  be solved, so we",
            "are adding more text",
            "to   see   that   it",
            "actually      works."
            ]
        result = justify_text(paragraph, width)
        self.assertEqual(result, expected_output)

    def test_lorem_ipsum(self):
        paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam."
        width = 20
        expected_output = [
            "Lorem   ipsum  dolor",
            "sit            amet,",
            "consectetur         ",
            "adipiscing     elit.",
            "Integer   nec  odio.",
            "Praesent libero. Sed",
            "cursus  ante dapibus",
            "diam.               "
            ]
        result = justify_text(paragraph, width)
        self.assertEqual(result, expected_output)

    def test_width_15(self):
        paragraph = "The quick brown fox jumps over the lazy dog."
        width = 15
        expected_output = [
            "The quick brown",
            "fox  jumps over",
            "the  lazy  dog."
            ]
        result = justify_text(paragraph, width)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
