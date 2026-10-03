import unittest
from small_function import trivial_function


class TestTrivialFunction(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(trivial_function(1, 2), 3)
        self.assertEqual(trivial_function(-1, -2), -3)
        self.assertEqual(trivial_function(-5, 5), 0)
        self.assertEqual(trivial_function(0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(trivial_function(1.5, 2.5), 4.0)
        self.assertAlmostEqual(trivial_function(0.1, 0.2), 0.3)
        self.assertAlmostEqual(trivial_function(-1.5, 0.5), -1.0)

    def test_strings(self):
        self.assertEqual(trivial_function("hello", " world"), "hello world")
        self.assertEqual(trivial_function("", "test"), "test")

    def test_lists(self):
        self.assertEqual(trivial_function([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(trivial_function([], [1]), [1])

    def test_incompatible_types_raise_type_error(self):
        with self.assertRaises(TypeError):
            trivial_function(1, "text")


if __name__ == "__main__":
    unittest.main()
