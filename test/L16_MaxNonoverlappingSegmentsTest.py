from unittest import TestCase
from codes.L16_MaxNonoverlappingSegments import solution


class MaxNonoverlappingSegmentsTest(TestCase):
    def test_sample(self):
        result = solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10])
        expect = 3
        self.assertEqual(expect, result)
