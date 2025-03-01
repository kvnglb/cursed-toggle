import os
import unittest

os.environ["SECRET_ENV_FOR_TESTING_ONLY_DO_NOT_USE"] = "3"

from cursed_toggle import cursed_toggle, _cursed_toggle


class TestCursedToggle(unittest.TestCase):
    def test_func_false(self):
        self.assertEqual(_cursed_toggle(False), 1)

    def test_func_true(self):
        self.assertEqual(_cursed_toggle(True), 0)

    def test_false(self):
        ans = cursed_toggle(False)
        self.assertTrue(ans)
        self.assertIsInstance(ans, bool)

    def test_true(self):
        ans = cursed_toggle(True)
        self.assertFalse(ans)
        self.assertIsInstance(ans, bool)

    def test_invalid_argument_0(self):
        self.assertRaises(TypeError, cursed_toggle, 0)


if __name__ == "__main__":
    unittest.main()
