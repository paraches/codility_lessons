from unittest import TestCase
from codes.L05_PassingCars import solution


class PassingCarsTest(TestCase):
    def test_sample(self):
        result = solution([0, 1, 0, 1, 1])
        expect = 5
        self.assertEqual(expect, result)
