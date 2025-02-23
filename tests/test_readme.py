import math
import re
import unittest


with open("README.md", "r") as file:
    lines = file.read()
fb = re.findall("^f\(b\).*=.*", lines, re.M)
funcs = []
for func in fb:
    funcs.append(func.split("=")[1])


class TestCursedToggle(unittest.TestCase):
    def test_func_false(self):
        for func in funcs:
            print(func)
            f = lambda b: eval(func)
            self.assertEqual(f(False), 1)

    def test_func_true(self):
        for func in funcs:
            print(func)
            f = lambda b: eval(func)
            self.assertEqual(f(True), 0)


if __name__ == "__main__":
    unittest.main()
