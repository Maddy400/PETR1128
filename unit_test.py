import unittest
import math
from calculator import evaluate_test

class TestCalculator(unittest.TestCase):

    def test_basic_operations(self):
        self.assertEqual(evaluate_test("2+3"), 5)
        self.assertEqual(evaluate_test("10-4"), 6)
        self.assertEqual(evaluate_test("3*4"), 12)
        self.assertEqual(evaluate_test("8/2"), 4)

    def test_advanced_math(self):
        self.assertAlmostEqual(evaluate_test("sqrt(16)"), 4)
        self.assertAlmostEqual(evaluate_test("log(100)"), 2)
        self.assertAlmostEqual(evaluate_test("sin(90)"), 1, places=5)
        self.assertAlmostEqual(evaluate_test("cos(0)"), 1, places=5)
        self.assertAlmostEqual(evaluate_test("tan(45)"), 1, places=5)

    def test_constants(self):
        self.assertAlmostEqual(evaluate_test("pi"), math.pi)
        self.assertAlmostEqual(evaluate_test("e"), math.e)

    def test_errors(self):
        self.assertEqual(evaluate_test("1/0"), "Error")
        self.assertEqual(evaluate_test("invalid"), "Error")

if __name__ == '__main__':
    unittest.main()
