import random

class MarkovGenerator:
    """
    This class converts text into a library for markov chain generation with certain depth. The latter defines the number of words in the current state, from which a new word is randomly chosen.
    """

    def __init__(self, depth=2, sentences=[]):
        self.depth = depth
        self.prefix_suffix_dict = dict()
        self.start_prefixes = []
        self.process_list_of_sentences(sentences)

    def process_list_of_sentences(self, sentences):
        for sentence in sentences:
            sentence.append("END_OF_SENTENCE")  # Add identifier for the end of a sentence.
            if len(sentence) > self.depth:  # Ignore sentences shorter than the depth
                tuple_list = self.parse_sentence(sentence)
                self.update_dict(tuple_list)

    def parse_sentence(self, sentence):
        text = sentence.copy()
        tuple_list = []

        tmp_tuple = tuple()
        for i in range(self.depth + 1):
            tmp_tuple = tmp_tuple + (text.pop(0),)
        tuple_list.append(tmp_tuple)
        # Add beginning of the sentence to to list, for drawing random starting points in generate_sentence()
        self.update_start_list(tmp_tuple)
        # Iterate through whole sentence
        while len(text) > 0:
            word = text.pop(0)
            tuple_list.append(self.shift(tuple_list[-1], word))
        return tuple_list

    @staticmethod
    def shift(prefix, word):
        return prefix[1:] + (word,)

    def update_dict(self, tuple_list):
        for t in tuple_list:
            prefix = t[:-1]
            suffix = t[-1]
            if prefix in self.prefix_suffix_dict:
                self.prefix_suffix_dict[prefix].append(suffix)
            else:
                self.prefix_suffix_dict[prefix] = [suffix]

    def update_start_list(self, start_prefix):
        self.start_prefixes.append(start_prefix)

    def generate_sentence(self):
        random_start = random.choice(self.start_prefixes)
        markov_text = list(random_start)
        #Loop until end of sentence is reached:
        while markov_text[-1] != "END_OF_SENTENCE":
            tmp_tuple = tuple(markov_text[-self.depth:])
            if tmp_tuple in self.prefix_suffix_dict:
                new_word = random.choice(self.prefix_suffix_dict[tmp_tuple])
                markov_text.append(new_word)
            else:
                print("Generated prefix has no suffix!")
        return markov_text[:-1] #Remove END_OF_SENTENCE flag from the end.
