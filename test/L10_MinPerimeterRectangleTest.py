from unittest import TestCase
from codes.L10_MinPerimeterRectangle import solution


class MinPerimeterRectangleTest(TestCase):
    def test_sample(self):
        result = solution(30)
        expect = 22
        self.assertEqual(expect, result)

    def test_one(self):
        result = solution(1)
        expect = 4
        self.assertEqual(expect, result)

    def test_1234(self):
        result = solution(1234)
        expect = 1238
        self.assertEqual(expect, result)
