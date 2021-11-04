import re
import nltk
from math import log, exp

# Global variables
# Are available within any function
START = "<START>"
STOP = "<STOP>"

def read_lines_from_file(fname):
    """read in a file and return a list of stripped lines
    input: 
        fname (str): file name to read
    returns:
        (list): list of lines from the file. Strip but do not lowercase or split. Do not return empty lines
    """
    ### YOUR CODE HERE
    ### The instructor solved this in 4 lines + the return
    lines = []
    return lines

def tokenize_words(line):
    """tokenize words in a line. Split off punctuation as their own tokens, do not lowercase
    input:
        line (str): text string
    return:
        (list): list of word or punctuation tokens, original casing
    """
    # YOUR CODE HERE
    ### The Instructor solved this in 1 line + the return
    tokenizedline = []
    return tokenizedline


def tokenize_chars(line):
    """tokenize characters in a line.
    input:
        line (str): text string
    return:
        (list): list of characters, orginal casing
    """
    ### YOUR CODE HERE
    ### The Instructor solved this in 1 line + the return
    tokenizedline = []
    return tokenizedline


def tokenize_wordchars(lines):
    """Turn a sequence of text lines into a series of character-tokenized words
    input:
        lines (seq): sequence of text strings
    return:
        (list): list of lists of characters
    """
    # YOUR CODE HERE
    ### The Instructor solved this in 3 line + the return
    tokenizedwords = []
    return tokenizedwords


def bigram_pad(seq):
    """Pad a sequence of tokens 
    input:
        seq (seq): sequence of tokens
        (tuple): tuple with START and STOP padding
    """
    ### YOUR CODE HERE
    ### The Instructor solved this in 1 line + the return
    padded = []
    return padded


def get_bigrams(seq):
    """Returns a list of bigrams with padding from a sequence
    input:
        seq (seq): sequence of tokens
    return:
        (list): list of bigrams from padded sequence
    """
    ### YOUR CODE HERE
    ### The Instructor solved this in 1 line + the return
    bigrams = []
    return bigrams


def update_freqdict(seq, freqdict):
    """updates a dictionary of frequencies
    input: 
        seq (sequence): token sequence
        freqdict (dict str:dict str:int): frequency dictionary mapping contexts to tokens, tokens to frequencies
    return:
        (none): the frequency dictionary is updated by-reference, not returned
    """
    ### YOUR CODE HERE
    ### The Instructor solved this in 7 line + the return
    return


def get_bigramlogprobs(freqdict):
    """converts a dicitonary of ngram frequencies into a dictionary of ngram log probabilities
    input:
        freqdict (dict str:dict str:num): frequency dict mapping contexts to tokens, tokens to frequencies
    return:
        (dict str:dict str:num): dict mapping contexts to tokens, tokens to log probabilities 
    """
    ### YOUR CODE HERE
    ### The Instructor solved this in 7 line + the return
    bigramlogprobdict = {}
    return bigramlogprobdict


def get_bigramlogprobs_fromcorpus(tokenizedseqs):
    """converts a list of tokenized lines into a dictionary of bigram log probabilities
    input:
        tokenizedlines (list): a list of tokenized lines. Each tokenized line is a list of tokens
    return:
        (dict str:dict str:num): dict mapping contexts to tokens, tokens to log probabilities 
    """
    ### YOUR CODE HERE
    ### The Instructor solved this in 3 line + the return
    freqdict = {}
    return get_bigramlogprobs(freqdict)


def score_sequence(seq, bigramlogprobs):
    """Scores a sequence of bigrams
    input:
        seq (seq): a sequence of bigrams
        bigramlogprobs (dict str:dict str:num): dict mapping contexts to tokens, tokens to log probabilities
    return:
        float('-inf') if any bigram is missing from bigramlogprobs. log probability of the sequence otherwise
    """
    ### YOUR CODE HERE
    ### The Instructor solved this in 8 line + the return
    score = 0
    return score


def main():

    # Some code that will be useful for answering the questions
    lines = read_lines_from_file("flatland_clean.txt")

    tokenizedlines = [tokenize_words(line) for line in lines]
    biprobs = get_bigramlogprobs_fromcorpus(tokenizedlines)

    tokenizedwords = tokenize_wordchars(lines)
    biprobs_w = get_bigramlogprobs_fromcorpus(tokenizedwords)

    ### YOU CAN WRITE YOUR OWN CODE HERE
    ### DO ANSWER THE QUESTIONS


    

if __name__ == "__main__":
    main()
