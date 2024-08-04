# main.py

import os
import pickle
from trie import Trie

def load_trie():
    data_directory = os.path.join(os.path.dirname(__file__), 'data')
    trie_path = os.path.join(data_directory, 'trie.pkl')
    with open(trie_path, 'rb') as f:
        trie = pickle.load(f)
    return trie

def find_words_recursive(trie, stem, remaining_string, found_words):
    if trie.is_valid_prefix(stem):
        if trie.find_words_with_prefix(stem):
            found_words.append(stem)
        for i in range(len(remaining_string)):
            find_words_recursive(trie, stem + remaining_string[i], remaining_string[i+1:], found_words)

if __name__ == "__main__":
    trie = load_trie()

    input_string = input("Enter the input string: ").replace(" ", "")
    found_words = []

    for i in range(len(input_string)):
        find_words_recursive(trie, input_string[i], input_string[i+1:], found_words)
    
    found_words = list(set(found_words))  # Remove duplicates
    found_words.sort()  # Optional: Sort the list of found words
    print(f"Found words: {found_words}")
