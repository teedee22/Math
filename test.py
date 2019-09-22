import unittest
from lina import inputRulesVector, convertToFloat, vectorSum


class TestinputRulesVectorVector(unittest.TestCase):
    """Tests inputRulesVector method with different valid and invalid inputs"""

    def test_correct_integer_input(self):
        self.assertEqual(inputRulesVector("3,4"), True, "Should be True")

    def test_correct_float_input(self):
        self.assertEqual(inputRulesVector("3.2,4.2"), True, "Should be True")

    def test_spaces_after_comma(self):
        self.assertEqual(inputRulesVector("3,     9"), True, "Should be True")

    def test_alphabetic_input(self):
        self.assertEqual(inputRulesVector("sdsdg, sdgdg"), False, "Should be False")

    def test_alphanumeric_input(self):
        self.assertEqual(inputRulesVector("3fr34, 43fer4f"), False, "Should be False")

    def test_no_comma(self):
        self.assertEqual(inputRulesVector("3034050948509345  390850943"), False, "Should be False")

    def test_too_many_commas(self):
        self.assertEqual(inputRulesVector("3, 4, 5"), False, "Should be False")


class TestConvertToFloat(unittest.TestCase):
    """Function must have passed inputRulesVector as true, tests it outputs correctly as float"""

    def test_converts_int_string_to_float(self):
        self.assertEqual(convertToFloat("3,4"), [3.0, 4.0])

    def test_converts_float_string_to_float(self):
        self.assertEqual(convertToFloat("3.345,9.235"), [3.345, 9.235])

# Test input rules number

# Test vector sum

# Test vector scale

if __name__ == '__main__':
    unittest.main()
