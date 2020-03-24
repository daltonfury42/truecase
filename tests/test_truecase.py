import os
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
