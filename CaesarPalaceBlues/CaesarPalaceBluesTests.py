import CaesarPalaceBlues
import unittest

class CaesarPalaceBluesTests(unittest.TestCase):

    # these tests had to be decommissioned when we decided that we could only have two functions

    """
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
    """

    def test_get_lower_character_number(self):
        self.assertEqual(CaesarPalaceBlues.get_character_number("e"), 4, "Should be 4")

    def test_get_upper_character_number(self):
        self.assertEqual(CaesarPalaceBlues.get_character_number("X"), 23, "Should be 23")

    def test_mixed_upper_and_lower_case(self):
        self.assertEqual(CaesarPalaceBlues.encrypt("LaunchCode", 13), "YnhapuPbqr", "Should be 'YnhapuPbqr'")

    def test_mixed_upper_and_lower_case_2(self):
        self.assertEqual(CaesarPalaceBlues.encrypt("LaunchCode", 1), "MbvodiDpef", "Should be 'MbvodiDpef'")

    def test_with_punctuation_and_space(self):
        self.assertEqual(CaesarPalaceBlues.encrypt("Hello, World!", 5), "Mjqqt, Btwqi!", "Should be 'Mjqqt, Btwqi!'")
   

if __name__ == "__main__":
    unittest.main()
