from unittest import TestCase
from codes.L09_MaxProfit import solution


class MaxProfitText(TestCase):
    def test_sample(self):
        result = solution([23171, 21011, 21123, 21366, 21013, 21367])
        expect = 356
        self.assertEqual(expect, result)
