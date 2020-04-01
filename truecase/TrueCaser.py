import math
import os
import pickle
import string

import nltk
from nltk.tokenize import TweetTokenizer


class TrueCaser(object):
    def __init__(self, dist_file_path=None):
        """ Initialize module with default data/english.dist file """
        if dist_file_path is None:
            dist_file_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "data/english.dist")

        with open(dist_file_path, "rb") as distributions_file:
            pickle_dict = pickle.load(distributions_file)
            self.uni_dist = pickle_dict["uni_dist"]
            self.backward_bi_dist = pickle_dict["backward_bi_dist"]
            self.forward_bi_dist = pickle_dict["forward_bi_dist"]
            self.trigram_dist = pickle_dict["trigram_dist"]
            self.word_casing_lookup = pickle_dict["word_casing_lookup"]
        self.tknzr = TweetTokenizer()

    def get_score(self, prev_token, possible_token, next_token):
        pseudo_count = 5.0

        # Get Unigram Score
        nominator = self.uni_dist[possible_token] + pseudo_count
        denominator = 0
        for alternativeToken in self.word_casing_lookup[
                possible_token.lower()]:
            denominator += self.uni_dist[alternativeToken] + pseudo_count

        unigram_score = nominator / denominator

        # Get Backward Score
        bigram_backward_score = 1
        if prev_token is not None:
            nominator = (
                self.backward_bi_dist[prev_token + "_" + possible_token] +
                pseudo_count)
            denominator = 0
            for alternativeToken in self.word_casing_lookup[
                    possible_token.lower()]:
                denominator += (self.backward_bi_dist[prev_token + "_" +
                                                      alternativeToken] +
                                pseudo_count)

            bigram_backward_score = nominator / denominator

        # Get Forward Score
        bigram_forward_score = 1
        if next_token is not None:
            next_token = next_token.lower()  # Ensure it is lower case
            nominator = (
                self.forward_bi_dist[possible_token + "_" + next_token] +
                pseudo_count)
            denominator = 0
            for alternativeToken in self.word_casing_lookup[
                    possible_token.lower()]:
                denominator += (
                    self.forward_bi_dist[alternativeToken + "_" + next_token] +
                    pseudo_count)

            bigram_forward_score = nominator / denominator

        # Get Trigram Score
        trigram_score = 1
        if prev_token is not None and next_token is not None:
            next_token = next_token.lower()  # Ensure it is lower case
            nominator = (self.trigram_dist[prev_token + "_" + possible_token +
                                           "_" + next_token] + pseudo_count)
            denominator = 0
            for alternativeToken in self.word_casing_lookup[
                    possible_token.lower()]:
                denominator += (
                    self.trigram_dist[prev_token + "_" + alternativeToken +
                                      "_" + next_token] + pseudo_count)

            trigram_score = nominator / denominator

        result = (math.log(unigram_score) + math.log(bigram_backward_score) +
                  math.log(bigram_forward_score) + math.log(trigram_score))

        return result

    def get_true_case(self, sentence, out_of_vocabulary_token_option="title"):
        """ Returns the true case for the passed tokens.

        @param tokens: Tokens in a single sentence
        @param outOfVocabulariyTokenOption:
            title: Returns out of vocabulary (OOV) tokens in 'title' format
            lower: Returns OOV tokens in lower case
            as-is: Returns OOV tokens as is
        """
        tokens = [t for t in sentence.split() if t != '']

        tokens_true_case = []
        for token_idx, token in enumerate(tokens):
            token_subs = nltk.word_tokenize(token)
            sub_true_case = []

            for token_sub in token_subs:
                if token_sub in string.punctuation or token_sub.isdigit():
                    sub_true_case.append(token_sub)
                else:
                    token_sub = token_sub.lower()
                    if token_sub in self.word_casing_lookup:
                        if len(self.word_casing_lookup[token_sub]) == 1:
                            sub_true_case.append(
                                list(self.word_casing_lookup[token_sub])[0])
                        else:
                            prev_token = (tokens[token_idx - 1]
                                        if token_idx > 0 else None)
                            next_token = (tokens[token_idx + 1]
                                        if token_idx < len(tokens) - 1 else None)

                            best_token = None
                            highest_score = float("-inf")

                            for possible_token in self.word_casing_lookup[token_sub]:
                                score = self.get_score(prev_token, possible_token,
                                                    next_token)

                                if score > highest_score:
                                    best_token = possible_token
                                    highest_score = score

                            sub_true_case.append(best_token)

                        if token_idx == 0:
                            sub_true_case[0] = sub_true_case[0].title()

                    else:  # Token out of vocabulary
                        if out_of_vocabulary_token_option == "title":
                            sub_true_case.append(token_sub.title())
                        elif out_of_vocabulary_token_option == "lower":
                            sub_true_case.append(token_sub.lower())
                        else:
                            sub_true_case.append(token_sub)
            tokens_true_case.append("".join(sub_true_case))

        return " ".join(tokens_true_case).strip()


if __name__ == "__main__":
    dist_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "data/english.dist")

    caser = TrueCaser(dist_file_path)

    while True:
        ip = input("Enter a sentence: ")
        print(caser.get_true_case(ip, "lower"))
