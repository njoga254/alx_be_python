import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance for use in tests."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various inputs."""
        self.assertEqual(self.calc.add(10, 5), 15)  # Positive numbers
        self.assertEqual(self.calc.add(-10, -5), -15)  # Negative numbers
        self.assertEqual(self.calc.add(10.5, 0.5), 11.0)  # Floating-point numbers
        self.assertEqual(self.calc.add(-10, 5), -5)  # Mixed positive and negative numbers

    def test_subtraction(self):
        """Test the subtraction method with various inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5)  # Positive numbers
        self.assertEqual(self.calc.subtract(-10, -5), -5)  # Negative numbers
        self.assertEqual(self.calc.subtract(10.5, 0.5), 10.0)  # Floating-point numbers
        self.assertEqual(self.calc.subtract(-10, 5), -15)  # Mixed positive and negative numbers

    def test_multiplication(self):
        """Test the multiplication method with various inputs."""
        self.assertEqual(self.calc.multiply(10, 5), 50)  # Positive numbers
        self.assertEqual(self.calc.multiply(-10, -5), 50)  # Negative numbers
        self.assertEqual(self.calc.multiply(10.5, 0.5), 5.25)  # Floating-point numbers
        self.assertEqual(self.calc.multiply(-10, 5), -50)  # Mixed positive and negative numbers

    def test_division(self):
        """Test the division method with various inputs."""
        self.assertEqual(self.calc.divide(10, 5), 2)  # Positive numbers
        self.assertEqual(self.calc.divide(-10, -5), 2)  # Negative numbers
        self.assertEqual(self.calc.divide(10.5, 0.5), 21.0)  # Floating-point numbers
        self.assertEqual(self.calc.divide(-10, 5), -2)  # Mixed positive and negative numbers

    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_division_with_zero_numerator(self):
        """Test division with a zero numerator."""
        self.assertEqual(self.calc.divide(0, 5), 0)  # 0 divided by any number should be 0

if __name__ == "__main__":
    unittest.main()
