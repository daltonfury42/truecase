from functools import lru_cache

from .TrueCaser import TrueCaser


@lru_cache(maxsize=1)
def get_truecaser():
    return TrueCaser()


def get_true_case(sentence, out_of_vocabulary_token_option='title'):
    return get_truecaser().get_true_case(sentence, out_of_vocabulary_token_option=out_of_vocabulary_token_option)
