import io
import os
import unittest
from contextlib import redirect_stdout

from src.path_check import path_checker


class TestPathChecker(unittest.TestCase):
    def test_path_checker_prints_and_returns_expected_parts(self):
        fake_file = os.path.join("C:\\repo", "Github_actions", "src", "path_check.py")

        stream = io.StringIO()
        with redirect_stdout(stream):
            returned_file, returned_dir, returned_folder = path_checker(fake_file)

        output = stream.getvalue()

        self.assertEqual(returned_file, fake_file)
        self.assertEqual(returned_dir, os.path.dirname(fake_file))
        self.assertEqual(returned_folder, os.path.basename(os.path.dirname(fake_file)))

        self.assertIn("File path:", output)
        self.assertIn("Directory path:", output)
        self.assertIn("Folder name:", output)


if __name__ == "__main__":
    unittest.main()
