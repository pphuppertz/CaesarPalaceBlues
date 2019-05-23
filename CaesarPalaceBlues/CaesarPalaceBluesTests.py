import CaesarPalaceBlues
import unittest

class CaesarPalaceBluesTests(unittest.TestCase):

    def test_rotate_lower(self):
        self.assertEqual(CaesarPalaceBlues.rotate_character("e", 5), "j", "Should be 'j'")

    def test_rotate_lower_rollover(self):
        self.assertEqual(CaesarPalaceBlues.rotate_character("x", 5), "c", "Should be 'c'")
        
    def test_rotate_upper(self):
        self.assertEqual(CaesarPalaceBlues.rotate_character("F", 7), "M", "Should be 'M'")

    def test_rotate_upper_rollover(self):
        self.assertEqual(CaesarPalaceBlues.rotate_character("W", 7), "D", "Should be 'D'")

    def test_rotate_should_not_be_equal(self):
        self.assertNotEqual(CaesarPalaceBlues.rotate_character("F", 7), "F", "Should be 'F'")

    def test_rotate_nonalpha(self):
        self.assertEqual(CaesarPalaceBlues.rotate_character("?", 7), "?", "Should be '?'")

    def test_get_lower_character_number(self):
        self.assertEqual(CaesarPalaceBlues.get_character_number("e"), 4, "Should be 4")

    def test_get_upper_character_number(self):
        self.assertEqual(CaesarPalaceBlues.get_character_number("X"), 23, "Should be 23")
   

if __name__ == "__main__":
    unittest.main()
