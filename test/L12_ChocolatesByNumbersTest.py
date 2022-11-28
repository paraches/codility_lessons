from unittest import TestCase
from codes.L12_ChocolatesByNumbers import solution


class ChocolatesByNumbersTest(TestCase):
    def test_sample(self):
        result = solution(10, 4)
        expect = 5
        self.assertEqual(expect, result)
