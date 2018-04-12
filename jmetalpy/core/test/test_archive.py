import unittest

from jmetalpy.core.archive import Archive
from jmetalpy.core.solution import Solution


class ArchiveTestCases(unittest.TestCase):
    def setUp(self):
        self.archive = Archive[Solution]()

    def test_should_constructor_create_a_non_null_object(self):
        self.assertIsNotNone(self.archive)

    def test_should_constructor_create_an_empty_list(self):
        self.assertEqual(0, len(self.archive.get_solution_list()))


if __name__ == '__main__':
    unittest.main()
