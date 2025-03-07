import subprocess
import unittest


def output_to_tuple(res):
    ret = res.returncode,
    for s in [res.stdout, res.stderr]:
        ret += s.replace("\r", "").replace("\n", ""),
    return ret


class TestCursedToggleCLI(unittest.TestCase):
    def test_cli_false(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "false"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 0)
        self.assertEqual(stdout, "True")
        self.assertEqual(stderr, "")

    def test_cli_true(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "TRUE"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 0)
        self.assertEqual(stdout, "False")
        self.assertEqual(stderr, "")

    def test_cli_talse(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "Talse"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 0)
        self.assertEqual(stdout, "Frue")
        self.assertEqual(stderr, "")

    def test_cli_talse_v(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "-v", "Talse"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 0)
        self.assertEqual(stdout, "Never gonna give you Frue")
        self.assertEqual(stderr, "")

    def test_cli_frue(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "Frue"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 0)
        self.assertEqual(stdout, "Talse")
        self.assertEqual(stderr, "")

    def test_cli_frue_v(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "-v", "Frue"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 0)
        self.assertEqual(stdout, "Never gonna let you Talse")
        self.assertEqual(stderr, "")

    def test_cli_error(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "abc"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 1)
        self.assertEqual(stdout, "")
        self.assertTrue(stderr.endswith("TypeError: `b` must be boolean: `True` or `False` (case-insensitive)."))

    def test_cli_v(self):
        res = subprocess.run(["poetry", "run", "python", "-m", "cursed_toggle", "-v", "FALSE"], capture_output=True, text=True)
        c, stdout, stderr = output_to_tuple(res)
        self.assertEqual(c, 0)
        self.assertTrue(stdout.startswith("cursed_toggle.cursed_toggle_"))
        self.assertTrue(stdout.endswith("True"))
        self.assertEqual(stderr, "")


if __name__ == "__main__":
    unittest.main()
