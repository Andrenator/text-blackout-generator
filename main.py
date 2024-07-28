# main.py

import pickle
from trie import Trie

# Load the Trie from the file
with open('trie.pkl', 'rb') as f:
    trie = pickle.load(f)

# Example Usage
prefix = "fin"
if trie.is_valid_prefix(prefix):
    print(f"'{prefix}' is a valid prefix.")
    words_with_prefix = trie.find_words_with_prefix(prefix)
    print(f"Words with prefix '{prefix}': {words_with_prefix}")
else:
    print(f"'{prefix}' is not a valid prefix.")
