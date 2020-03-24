import os
import unittest

from truecase import Trainer


class TestTrainer(unittest.TestCase):

    def setUp(self):
        self.tc = Trainer.Trainer()

    def test_get_casing(self):
        word = ''
        result = self.tc.get_casing(word)

        assert result == 'other'

        word = '1'
        result = self.tc.get_casing(word)

        assert result == 'numeric'

        word = 'low_word'
        result = self.tc.get_casing(word)

        assert result == 'allLower'

        word = 'ALL_UPPER'
        result = self.tc.get_casing(word)

        assert result == 'allUpper'

        word = 'Initial'
        result = self.tc.get_casing(word)

        assert result == 'initialUpper'

        word = '_.,:;'
        result = self.tc.get_casing(word)

        assert result == 'other'
