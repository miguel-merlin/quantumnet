import unittest
from src.linearalgebra.vector import Vector

class TestVector(unittest.TestCase):
    def test_dot_product(self):
        vector1 = Vector([5,3])
        vector2 = Vector([10,2])
        self.assertEqual(vector1.dot_product(vector2), 56)


if __name__ == '__main__':
    unittest.main()