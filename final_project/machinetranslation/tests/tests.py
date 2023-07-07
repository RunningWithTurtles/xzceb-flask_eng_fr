import unittest

class TranslationTest(unittest.TestCase):
    def test_frenchToEnglish(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        
        result = frenchToEnglish(french_text)
        
        self.assertEqual(result, expected_english_text)
    def test_frenchToEnglish(self):
        french_text = "Au Revoir"
        expected_english_text = "Goodbye"
        
        result = frenchToEnglish(french_text)
        
        self.assertEqual(result, expected_english_text)
    def test_englishToFrench(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        
        result = englishToFrench(english_text)
        
        self.assertEqual(result, expected_french_text)
    def test_englishToFrench(self):
        english_text = "Goodbye"
        expected_french_text = "Au Revoir"
        
        result = englishToFrench(english_text)
        
        self.assertEqual(result, expected_french_text)

if __name__ == '__main__':
    unittest.main()
