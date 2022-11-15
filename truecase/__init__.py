from functools import lru_cache
from .Trainer import Trainer
from .TrueCaser import TrueCaser

__version__ = "0.0.14"


@lru_cache(maxsize=1)
def get_truecaser(dist_file_path=None):
    return TrueCaser(dist_file_path)


def get_true_case(sentence, out_of_vocabulary_token_option="title"):
    return get_truecaser().get_true_case(
        sentence,
        out_of_vocabulary_token_option=out_of_vocabulary_token_option)
