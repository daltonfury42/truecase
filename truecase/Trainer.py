import nltk
import pickle

class Trainer(object):

    def __init__(self):
        self.uni_dist = None
        self.backward_bi_dist = None
        self.forward_bi_dist = None
        self.trigram_dist = None
        self.word_casing_lookup = None

    def init(self):
        self.uni_dist = nltk.FreqDist()
        self.backward_bi_dist = nltk.FreqDist()
        self.forward_bi_dist = nltk.FreqDist()
        self.trigram_dist = nltk.FreqDist()
        self.word_casing_lookup = {}

    def train(self, corpus):

        self.init()

        for sentence in corpus:
            if not self.check_sentence_sanity(sentence):
                continue

            for word_idx, word in enumerate(sentence):
                self.uni_dist[word] += 1
                word_lower = word.lower()
                if word_lower not in self.word_casing_lookup:
                    self.word_casing_lookup[word_lower] = set()

                self.word_casing_lookup[word_lower].add(word)

                try:
                    if word_lower in self.word_casing_lookup and len(self.word_casing_lookup[word_lower]) >= 2:
                        # Only if there are multiple options
                        prev_word = sentence[word_idx - 1]

                        self.backward_bi_dist[prev_word + "_" + word] += 1

                        next_word = sentence[word_idx + 1].lower()
                        self.forward_bi_dist[word + "_" + next_word] += 1
                except IndexError:
                    pass

                try:
                    if word_idx - 1 < 0:
                        continue

                    prev_word = sentence[word_idx - 1]
                    cur_word = sentence[word_idx]
                    cur_word_lower = word.lower()
                    next_word_lower = sentence[word_idx + 1].lower()

                    if cur_word_lower in self.word_casing_lookup and len(self.word_casing_lookup[cur_word_lower]) >= 2:
                        # Only if there are multiple options
                        self.trigram_dist[prev_word + "_" + cur_word + "_" + next_word_lower] += 1
                except IndexError:
                    pass

    def save_to_file(self, file_path):
        pickle_dict = {
            'uni_dist': self.uni_dist,
            'backward_bi_dist': self.backward_bi_dist,
            'forward_bi_dist': self.forward_bi_dist,
            'trigram_dist': self.trigram_dist,
            'word_casing_lookup': self.word_casing_lookup,
        }

        with open(file_path, "wb") as fp:
            pickle.dump(pickle_dict, fp)

        print('Model saved to ' + file_path)

    def get_casing(self, word):
        """ Returns the casing of a word"""
        if len(word) == 0:
            return 'other'
        elif word.isdigit():  # Is a digit
            return 'numeric'
        elif word.islower():  # All lower case
            return 'allLower'
        elif word.isupper():  # All upper case
            return 'allUpper'
        elif word[0].isupper():  # is a title, initial char upper, then all lower
            return 'initialUpper'

        return 'other'

    def check_sentence_sanity(self, sentence):
        """ Checks the sanity of the sentence. If the sentence is for example all uppercase, it is recjected"""
        case_dist = nltk.FreqDist()

        for token in sentence:
            case_dist[self.get_casing(token)] += 1

        if case_dist.most_common(1)[0][0] != 'allLower':
            return False

        return True

if __name__ == '__main__':
    corpus = nltk.corpus.brown.sents()  \
             + nltk.corpus.reuters.sents() \
             + nltk.corpus.semcor.sents() \
             + nltk.corpus.conll2000.sents() \
             + nltk.corpus.state_union.sents()


    trainer = Trainer()
    trainer.train(corpus)

    trainer.save_to_file('data/english.dist')