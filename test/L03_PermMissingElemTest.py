from unittest import TestCase
from code.L03_PermMissingElem import solution


class PermMissingElemTest(TestCase):
    def test_sample(self):
        result = solution([2, 3, 1, 5])
        expect = 4
        self.assertEqual(expect, result)

    def test_zero_array(self):
        result = solution([])
        expect = 1
        self.assertEqual(expect, result)
