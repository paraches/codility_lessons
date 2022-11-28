from unittest import TestCase
from codes.L09_MaxSliceSum import solution


class MaxSliceSumTest(TestCase):
    def test_sample(self):
        result = solution([3, 2, -6, 4, 0])
        expect = 5
        self.assertEqual(expect, result)
