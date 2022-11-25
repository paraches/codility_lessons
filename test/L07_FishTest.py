from unittest import TestCase
from codes.L07_Fish import solution


class FishTest(TestCase):
    def test_sample(self):
        result = solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])
        expect = 2
        self.assertEqual(expect, result)
