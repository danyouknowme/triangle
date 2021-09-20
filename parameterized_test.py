import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):

  valid_triangles = [
    (1, 1, 1),
    (3, 4, 5),
    (3, 4, 6),  
  ]

  def test_valid_triangle(self):
    for a,b,c in self.valid_triangles:
      with self.subTest():
        msg = f"side lengths ({a},{b},{c})"
        self.assertTrue( is_triangle(a, b, c), msg)

  invalid_triangles = [
    (14, 4, 6),
    (4, 2, 2),
    (3, 18, 9),
    (5, 10, 5),
    (2, 6, 14)
  ]

  def test_invalid_triangle(self):
    for a,b,c in self.invalid_triangles:
      with self.subTest():
        msg = f"side lengths ({a},{b},{c})"
        self.assertFalse( is_triangle(a, b, c), msg)

  invalid_arguments = [
    (-10, 2, 4),
    (3, -5, 6),
    (-1, -2, -3),
    (14, 8, -3)
  ]

  def test_invalid_argument(self):
    """any non-positive number should raise ValueError"""
    for a, b, c in self.invalid_arguments:
      with self.subTest():
        self.assertRaises(ValueError, is_triangle(a, b, c))

