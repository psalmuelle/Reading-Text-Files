# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from curses import KEY_UNDO
from operator import contains
from os import listdir
from zlib import Z_TREES
import string


def read_file_content(filename):
   with open(filename) as story:
       contents = story.read()
       return contents


def count_words():
    texts = read_file_content("./story.txt")
    texts = texts.lower().split()
    texts.sort()
    

    list_of_words = texts
    all_punctuation = str.maketrans("", "", string.punctuation)
    formatted_words = [w.translate(all_punctuation) for w in list_of_words]

    counts = {}
    

    for i in range(len(formatted_words)):

        counts[formatted_words[i]] = formatted_words.count(formatted_words[i])


    return counts

print(count_words())

