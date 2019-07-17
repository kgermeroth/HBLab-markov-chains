"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    the_file = open(file_path)
    file_text = the_file.read()

    words = file_text.split()

    the_file.close()

    return words


# def make_chains(words):
#     """Take input text as string; return dictionary of Markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> chains = make_chains("hi there mary hi there juanita")

#     Each bigram (except the last) will be a key in chains:

#         >>> sorted(chains.keys())
#         [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

#     Each item in chains is a list of all possible following words:

#         >>> chains[('hi', 'there')]
#         ['mary', 'juanita']
        
#         >>> chains[('there','juanita')]
#         [None]
#     """

#     chains = {}


#     # loop through list of words, create tuples of bigrams
#     # see if tuple is already in dictionary, if not add to dictionary, else append next word
#     for i, word in enumerate(words):
#         if i < len(words) - 2:
#             bigram_tuple = (word, words[i + 1])
            
#             if chains.get(bigram_tuple) == None:
#                 chains[bigram_tuple] = [words[i + 2]]

#             else:
#                 chains[bigram_tuple].append(words[i + 2])

#     return chains


def make_chains(words, n_words):
    """Take input text as string; return dictionary of Markov chains.

    """

    chains = {}


    # loop through list of words, create tuples of bigrams
    # see if tuple is already in dictionary, if not add to dictionary, else append next word
    for i, word in enumerate(words):
        if i < len(words) - n_words:
            ngram_tuple = tuple(words[i:n_words + i])
            
            if chains.get(ngram_tuple) == None:
                chains[ngram_tuple] = [words[i + n_words]]

            else:
                chains[ngram_tuple].append(words[i + n_words])

    return chains


def make_text(chains, n_words):
    """Return text from chains."""

    words = []

    # if you want to start with random tuple:    
    tuple_in_use = choice(list(chains))

    words.extend(tuple_in_use)

    # loop until the tuple is not a key
    while True:
        if chains.get(tuple_in_use) == None:
            break
    
    # choose random list item from that key as next word 
        else:    
            next_word = choice(list(chains[tuple_in_use]))
            
            words.append(next_word)

            # set the next tuple to use as a key
            tuple_in_use = tuple(words[n_words * -1:])

    return " ".join(words)

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

n_gram = int(input("How many words in your n-gram? "))

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = make_text(chains, n_gram)

print(random_text)