from markov_generator import MarkovGenerator
from nltk.corpus import gutenberg
from nltk.tokenize.treebank import TreebankWordDetokenizer

markov = MarkovGenerator(3, gutenberg.sents())
markov_text = markov.generate_sentence()

print(TreebankWordDetokenizer().detokenize(markov_text))
