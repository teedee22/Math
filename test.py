import unittest
from helpers import inputRulesVector, convertToFloat, inputRulesNumber
from lina import vectorSum, vectorScale, vectorTransform, matrixMultiplication


class TestinputRulesVector(unittest.TestCase):
    """Tests inputRulesVector method with different valid and invalid inputs"""

    def test_allows_integer_input(self):
        self.assertEqual(inputRulesVector("3,4", 2), True, "Should be True")

    def test_allows_float_input(self):
        self.assertEqual(inputRulesVector("3.2,4.2", 2), True, "Should be True")

    def test_allows_spaces_after_comma(self):
        self.assertEqual(inputRulesVector("3,     9", 2), True, "Should be True")

    def test_allows_negative_input(self):
        self.assertEqual(inputRulesVector("-32.1, -7.5", 2), True)

    def test_allows_zero_input(self):
        self.assertEqual(inputRulesVector("0, 0", 2), True)

    def test_denies_alphabetic_input(self):
        self.assertEqual(inputRulesVector("sdsdg, sdgdg", 2), False, "Should be False")

    def test_denies_alphanumeric_input(self):
        self.assertEqual(inputRulesVector("3fr34, 43fer4f", 2), False, "Should be False")

    def test_denies_no_comma(self):
        self.assertEqual(inputRulesVector("3034050948509345  390850943", 2), False, "Should be False")

    def test_accepts_more_then_two_inputs(self):
        self.assertEqual(inputRulesVector("3, 4, 5, 6", 4), True,)


class TestConvertToFloat(unittest.TestCase):
    """Function must have passed inputRulesVector as true, tests it outputs correctly as float"""

    def test_converts_int_string_to_float(self):
        self.assertEqual(convertToFloat("3,4"), [3.0, 4.0])

    def test_converts_matrices_to_float(self):
        self.assertEqual(convertToFloat("1,2,3,4"), [1.0, 2.0, 3.0, 4.0])

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


class TestVectorScale(unittest.TestCase):
    """test that vectorScale returns scaled vector"""

    def test_allows_integer_input(self):
        self.assertEqual(vectorScale([3, 4], 5), [15, 20])

    # This test caused me to round the numbers as floating point was generating inaccuracies
    def test_allows_float_input(self):
        self.assertEqual(vectorScale([3.2, 3.8], 6.3), [20.16, 23.94])

    def test_allows_negative_input(self):
        self.assertEqual(vectorScale([-3, -0.5], -1), [3, 0.5])

    def test_allows_zero_input(self):
        self.assertEqual(vectorScale([0, 0], 0), [0, 0])

    def test_allows_3d_input(self):
        self.assertEqual(vectorScale([4, 8, 2], 2), [8, 16, 4])


class TestVectorTransform(unittest.TestCase):
    """Test that VectorTransform works"""

    def test_allows_integer_input(self):
        self.assertEqual(vectorTransform([1, -2, 3, 0], [-1, 2]), [5.0, 2.0])

    def test_allows_float_input(self):
        self.assertEqual(vectorTransform([-1, 3.6, 4, 3.1], [2.7, 0.2]), [-1.9, 10.34])

    def test_allows_zero_input(self):
        self.assertEqual(vectorTransform([0, 0, 0, 0], [0, 0]), [0, 0])

    def test_allows_3d_input(self):
        self.assertEqual(vectorTransform([0,5,1,-2,1,4,2,5,-1], [2,5,8]), [6, 55, 14])


class TestMatrixMultiplication(unittest.TestCase):
    """Test that matrix multiplication works"""

    def test_allows_integer_input(self):
        self.assertEqual(matrixMultiplication([1, 3, 5, 7], [2, 5, 6, 8]), [20, 29, 52, 81])

    def test_allows_float_input(self):
        self.assertEqual(matrixMultiplication([1.5, 2.5, 6.5, 4.5], [1, 2, 3, 4]), [9.0, 13.0, 20.0, 31.0])

    def test_allows_negative_input(self):
        self.assertEqual(matrixMultiplication([0, 0, 0, 0], [0, 0, 0, 0]), [0, 0, 0, 0])

    def test_allows_three_dimensions(self):
        self.assertEqual(matrixMultiplication([0,3,6,1,4,7,2,5,8], [0,5,1,-2,1,4,2,5,-1]), [6.0, 33.0, 6.0, 6.0, 44.0, 10.0, 6.0, 55.0, 14.0])

if __name__ == '__main__':
    unittest.main()
