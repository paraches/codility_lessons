from unittest import TestCase
from code.L03_FromJmp import solution


class FrogJmpTest(TestCase):
    def test_sample(self):
        result = solution(10, 85, 30)
        expect = 3
        self.assertEqual(expect, result)
