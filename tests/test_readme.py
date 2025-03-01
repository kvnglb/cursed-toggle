import math
import re
import time
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
            for t in range(10, 14):
                print(f"t={t}", func)
                f = lambda b,t: eval(func)  # weird that t stays t (therefore `lambda b,t`), but only in the test. If the function is forged without unittest, t from the loop is taken.
                self.assertEqual(f(False, t), 1)

    def test_func_true(self):
        for func in funcs:
            for t in range(10, 14):
                print(f"t={t}", func)
                f = lambda b,t: eval(func)  # same as above
                self.assertEqual(f(True, t), 0)


if __name__ == "__main__":
    unittest.main()
