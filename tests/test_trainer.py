import unittest

from truecase import Trainer


class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.tc = Trainer.Trainer()

    def test_get_casing(self):
        word = ""
        result = self.tc.get_casing(word)

        assert result == "other"

        word = "1"
        result = self.tc.get_casing(word)

        assert result == "numeric"

        word = "low_word"
        result = self.tc.get_casing(word)

        assert result == "allLower"

        word = "ALL_UPPER"
        result = self.tc.get_casing(word)

        assert result == "allUpper"

        word = "Initial"
        result = self.tc.get_casing(word)

        assert result == "initialUpper"

        word = "_.,:;"
        result = self.tc.get_casing(word)

        assert result == "other"

    def test_check_sentence_sanity(self):
        sentence = "TO BE REJECTED"
        result = self.tc.check_sentence_sanity(sentence)

        assert not result

        sentence = "to be accepted"
        result = self.tc.check_sentence_sanity(sentence)

        assert result

        sentence = "I live in Barcelona not Chicago nor New York"
        result = self.tc.check_sentence_sanity(sentence)

        assert result

        sentence = "ALERT this is a warning"
        result = self.tc.check_sentence_sanity(sentence)

        assert result
