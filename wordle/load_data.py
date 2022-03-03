from os.path import exists

from wget import download

from wordle.constants import (
    ALLOWED_ANSWERS_URL, 
    ALLOWED_ANSWERS_FILENAME,
    ALLOWED_GUESSES_URL, 
    ALLOWED_GUESSES_FILENAME)


def read_word_list_file(filename):
    """
    Reads a text word list into a list of words, each of which have length word_length
    """
    with open(filename, 'r') as fh:
        return [line.strip() for line in fh]


def load_word_lists():
    """
    Returns the word lists of allowed guesses and allowed answers
    If word lists aren't present, download them.
    """
    if not exists(ALLOWED_GUESSES_FILENAME):
        download(ALLOWED_GUESSES_URL, ALLOWED_GUESSES_FILENAME)
    if not exists(ALLOWED_ANSWERS_FILENAME):
        download(ALLOWED_ANSWERS_URL, ALLOWED_ANSWERS_FILENAME)
    return read_word_list_file(ALLOWED_GUESSES_FILENAME), read_word_list_file(ALLOWED_ANSWERS_FILENAME)