import unittest
from normalizer import TextNormalizer

class TestTextNormalizer(unittest.TestCase):
    def setUp(self):
        self.normalizer = TextNormalizer()

    def test_basic_normalization(self):
        self.assertEqual(
            self.normalizer.normalize_query("  Hello,   WORLD!  "),
            "hello world"
        )

    def test_lemmatization(self):
        self.assertEqual(
            self.normalizer.normalize_query("running runners ran"),
            "run runner run"
        )
    def test_lemmatization2(self):
        self.assertEqual(
            self.normalizer.normalize_query("refund policies"),
            "refund policy"
        )

    def test_stopword_removal(self):
        self.assertEqual(
            self.normalizer.normalize_query("This is a test of the emergency broadcast system"),
            "test emergency broadcast system"
        )    

    def test_date_normalization(self):
        result = self.normalizer.normalize_query("I will travel tomorrow")
        self.assertIn("travel", result)
        # Should contain a normalized date string
        self.assertRegex(result, r"\d{4}-\d{2}-\d{2}")

    def test_money_and_numbers(self):
        text = "Hotels in NYC around $200 per night !!!"
        result = self.normalizer.normalize_query(text)
        self.assertEqual(result, "hotel nyc around 200 per night")

    def test_no_false_date(self):
        # "one" should not be normalized to a date
        self.assertIn("one", self.normalizer.normalize_query("one apple"))

    def test_entity_normalization(self):
        text = "AI startups & venture capital"
        result = self.normalizer.normalize_query(text)
        self.assertEqual(result, "ai startups venture capital")
    
    def test_entity_normalization2(self):
        text="I have two apples and 3 bananas"
        result = self.normalizer.normalize_query(text)
        self.assertEqual(result, "two apple 3 banana")
        
    def test_named_entity_recognition(self):
        text = "How to troubleshoot the server error issue in New York?"
        result = self.normalizer.normalize_query(text)
        self.assertEqual(result, "troubleshoot server error issue gpe")
        
    def test_unicode_normalization(self):
        # Test for the "ﬁ" (U+FB01) ligature character, which should normalize to "fi"
        text = "office ﬁle"
        result = self.normalizer.normalize_query(text)
        self.assertIn("office", result)
        self.assertIn("file", result)
        

if __name__ == "__main__":
    unittest.main()