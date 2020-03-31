import unittest

import truecase


class TestTrueCase(unittest.TestCase):
    def setUp(self):
        self.tc = truecase.TrueCaser()

    def test_get_true_case(self):
        sentence = "I live in barcelona."
        expected = "I live in Barcelona."

        result = self.tc.get_true_case(sentence)

        assert result == expected

        sentence = "My name is irvine wels"
        expected = "My name is Irvine Wels"

        result = self.tc.get_true_case(sentence)

        assert result == expected

    def test_fix_upper_contractions(self):
        sentence = "isn'T"
        expected = "isn't"

        result = self.tc._fix_upper_contractions(sentence)

        assert result == expected
