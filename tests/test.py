import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator.functions import evaluate_expression

class TestEvaluateExpression(unittest.TestCase):
    def test_arithmetic_operations(self):
        self.assertEqual(evaluate_expression("2 + 3"), "5.0")
        self.assertEqual(evaluate_expression("5 - 3"), "2.0")
        self.assertEqual(evaluate_expression("4 * 3"), "12.0")
        self.assertEqual(evaluate_expression("8 / 2"), "4.0")

    def test_trigonometric_functions(self):
        self.assertEqual(evaluate_expression("sin(π/2)"), "1.0")
        self.assertEqual(evaluate_expression("cos(π)"), "-1.0")

    def test_logarithmic_functions(self):
        self.assertEqual(evaluate_expression("ln(e)"), "1.0")
        self.assertEqual(evaluate_expression("log(100)"), "2.0")

    def test_factorial(self):
        self.assertEqual(evaluate_expression("factorial(5)"), "120.0")

    def test_error_handling(self):
        self.assertTrue("Error" in evaluate_expression("sin(/)"))

if __name__ == '__main__':
    unittest.main()
