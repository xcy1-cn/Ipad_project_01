"""Run from the repository root: python3 -m unittest discover -s tests -v."""

import unittest

from examples.hello import greeting


class GreetingTests(unittest.TestCase):
    def test_default_name(self):
        self.assertEqual(greeting(), "Hello, iPad!")

    def test_custom_name(self):
        self.assertEqual(greeting("  小明  "), "Hello, 小明!")

    def test_blank_name_uses_default(self):
        self.assertEqual(greeting("   "), "Hello, iPad!")


if __name__ == "__main__":
    unittest.main()
