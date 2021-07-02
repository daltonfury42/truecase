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

        sentence = "i paid $50 FOR My shoes."
        expected = "I paid $50 for my shoes."
        result = self.tc.get_true_case(sentence)
        assert result == expected

        sentence = "Ron'S show Is a big Hit."
        expected = "Ron's show is a big hit."
        result = self.tc.get_true_case(sentence)
        assert result == expected

        sentence = "What Is Your name?"
        expected = "What is your name?"
        result = self.tc.get_true_case(sentence)
        assert result == expected

        sentence = "at The moment, I AM getting ready for work!"
        expected = "At the moment, I am getting ready for work!"
        result = self.tc.get_true_case(sentence)
        assert result == expected
                
        sentence = "Please don't ruin the apostrophe."
        expected = "Please don't ruin the apostrophe."
        result = self.tc.get_true_case(sentence)
        assert result == expected
                
        sentence = "Testing $bug"
        expected = "Testing $bug"
        result = self.tc.get_true_case(sentence)
        assert result == expected
