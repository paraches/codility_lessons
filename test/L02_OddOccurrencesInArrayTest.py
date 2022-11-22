from unittest import TestCase
from code.L02_OddOccurrencesInArray import solution


class OddOccurrencesInArray(TestCase):
    def test_sample(self):
        result = solution([9, 3, 9, 3, 9, 7, 9])
        expect = 7
        self.assertEqual(expect, result)
