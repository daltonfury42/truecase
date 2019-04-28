from .TrueCaser import TrueCaser

caser = TrueCaser()

def get_true_case(sentence, out_of_vocabulary_token_option='title'):

    return caser.get_true_case(sentence, out_of_vocabulary_token_option=out_of_vocabulary_token_option)

