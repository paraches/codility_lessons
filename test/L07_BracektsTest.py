from unittest import TestCase
from codes.L07_Brackets import solution


class BracketsTest(TestCase):
    def test_sample_true(self):
        result = solution('{[()()]}')
        expect = 1
        self.assertEqual(expect, result)

    def test_sample_false(self):
        result = solution('([)()]')
        expect = 0
        self.assertEqual(expect, result)

    def test_zero(self):
        result = solution('')
        expect = 1
        self.assertEqual(expect, result)
