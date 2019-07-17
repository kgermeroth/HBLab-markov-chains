"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_paths):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    combined_text = ""

    files = file_paths[1:]

    for poem in files:
        the_file = open(poem)
        file_text = the_file.read()

        combined_text += file_text
        the_file.close()

    words = combined_text.split()

    return words


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
    while True:
        tuple_in_use = choice(list(chains))

        if tuple_in_use[0][0].isupper():
            break

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
# input_text = open_and_read_file(sys.argv[1], sys.argv[2])
input_text = open_and_read_file(sys.argv)

n_gram = int(input("How many words in your n-gram? "))

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = make_text(chains, n_gram)

print(random_text)