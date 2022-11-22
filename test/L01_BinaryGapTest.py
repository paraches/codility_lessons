from unittest import TestCase
from code.L01_BinaryGap import solution


class BinaryGapTest(TestCase):
    def test_sample_9(self):
        result = solution(9)
        expect = 2
        self.assertEqual(expect, result)

    def test_sample_529(self):
        result = solution(529)
        expect = 4
        self.assertEqual(expect, result)

    def test_sample_20(self):
        result = solution(20)
        expect = 1
        self.assertEqual(expect, result)

    def test_sample_15(self):
        result = solution(15)
        expect = 0
        self.assertEqual(expect, result)

    def test_sample_32(self):
        result = solution(32)
        expect = 0
        self.assertEqual(expect, result)

    def test_sample_1041(self):
        result = solution(1041)
        expect = 5
        self.assertEqual(expect, result)
