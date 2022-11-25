from unittest import TestCase
from codes.L08_EquiLeader import solution


class EquiLeaderTest(TestCase):
    def test_sample(self):
        result = solution([4, 3, 4, 4, 4, 2])
        expect = 2
        self.assertEqual(expect, result)
