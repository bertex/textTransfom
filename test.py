import unittest
import transfom


class TestStringMethods(unittest.TestCase):

    def test_is_upper(self):
        sting = transfom.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        sting = transfom.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        sting = transfom.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
