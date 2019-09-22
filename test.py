import unittest
from lina import inputRulesVector, convertToFloat, vectorSum, inputRulesNumber


class TestinputRulesVector(unittest.TestCase):
    """Tests inputRulesVector method with different valid and invalid inputs"""

    def test_allows_integer_input(self):
        self.assertEqual(inputRulesVector("3,4"), True, "Should be True")

    def test_allows_float_input(self):
        self.assertEqual(inputRulesVector("3.2,4.2"), True, "Should be True")

    def test_allows_spaces_after_comma(self):
        self.assertEqual(inputRulesVector("3,     9"), True, "Should be True")

    def test_allows_negative_input(self):
        self.assertEqual(inputRulesVector("-32.1, -7.5"), True)

    def test_allows_zero_input(self):
        self.assertEqual(inputRulesVector("0, 0"), True)

    def test_denies_alphabetic_input(self):
        self.assertEqual(inputRulesVector("sdsdg, sdgdg"), False, "Should be False")

    def test_denies_alphanumeric_input(self):
        self.assertEqual(inputRulesVector("3fr34, 43fer4f"), False, "Should be False")

    def test_denies_no_comma(self):
        self.assertEqual(inputRulesVector("3034050948509345  390850943"), False, "Should be False")

    def test_denies_too_many_commas(self):
        self.assertEqual(inputRulesVector("3, 4, 5"), False, "Should be False")


class TestConvertToFloat(unittest.TestCase):
    """Function must have passed inputRulesVector as true, tests it outputs correctly as float"""

    def test_converts_int_string_to_float(self):
        self.assertEqual(convertToFloat("3,4"), [3.0, 4.0])

    def test_converts_float_string_to_float(self):
        self.assertEqual(convertToFloat("3.345,9.235"), [3.345, 9.235])

    def test_converts_negative_to_float(self):
        self.assertEqual(convertToFloat("-2.3, -2.5"), [-2.3, -2.5])

    def test_converts_zero_to_float(self):
        self.assertEqual(convertToFloat("0, 0"), [0, 0])


class TestInputRulesNumber(unittest.TestCase):
    """tests that the inputRulesNumber accepts only ints and floats"""

    def test_accepts_int(self):
        self.assertEqual(inputRulesNumber("3"), True)

    def test_accepts_float(self):
        self.assertEqual(inputRulesNumber("3.5"), True)

    def test_accepts_negative(self):
        self.assertEqual(inputRulesNumber("-10"), True)

    def test_rejects_letters(self):
        self.assertEqual(inputRulesNumber("hello"), False)

    def test_rejects_letters_and_numbers(self):
        self.assertEqual(inputRulesNumber("h377o"), False)

    def test_rejects_no_input(self):
        self.assertEqual(inputRulesNumber(""), False)


# Test vector sum
class TestVectorSum(unittest.TestCase):
    """Test that vectorSum returns linear combination of two lists of floats and outputs a tuple"""

    def test_correct_addition_ints(self):
        self.assertEqual(vectorSum([1, 2], [3, 4]), (4, 6), "must output a tuple")

    def test_correct_addition_floats(self):
        self.assertEqual(vectorSum([1.5, 2.5], [3.7, 2.6]), (5.2, 5.1))

    def test_correct_zero_addition(self):
        self.assertEqual(vectorSum([0, 0], [0, 0]), (0, 0))

    def test_correct_negative_addition(self):
        self.assertEqual(vectorSum([-3, -123.2], [12, -1]), (9, -124.2))
# Test vector scale


if __name__ == '__main__':
    unittest.main()
