# build_trie.py

import os
import pickle
from trie import Trie

def build_trie_from_files(directory):
    trie = Trie()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                words = f.read().split()
                for word in words:
                    trie.insert(word)
    return trie

if __name__ == "__main__":
    data_directory = os.path.join(os.path.dirname(__file__), 'data')
    trie = build_trie_from_files(data_directory)
    
    # Save the Trie to a file in the data directory
    with open(os.path.join(data_directory, 'trie.pkl'), 'wb') as f:
        pickle.dump(trie, f)
