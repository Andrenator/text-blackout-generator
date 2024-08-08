import os
import pickle
from trie import Trie

def load_trie():
    data_directory = os.path.join(os.path.dirname(__file__), 'data')
    trie_path = os.path.join(data_directory, 'trie.pkl')
    with open(trie_path, 'rb') as f:
        trie = pickle.load(f)
    return trie

def find_words_recursive(trie, stem, remaining_string, found_words, start_index, original_length):
    if trie.is_valid_prefix(stem):
        if trie.is_complete_word(stem):  # Check if the stem is a complete word
            end_index = original_length - len(remaining_string)
            found_words.append((stem, start_index, end_index))
        counter = 0
        while counter < len(remaining_string):
            find_words_recursive(trie, stem + remaining_string[counter], remaining_string[counter+1:], found_words, start_index, original_length)
            while counter + 1 < len(remaining_string) and remaining_string[counter] != " ":
                counter += 1
            counter += 1

def replace_words_in_text(input_string, found_words):
    result = []
    last_index = 0
    
    for word, start, end in found_words:
        left = input_string[:start]
        right = input_string[end:]

        while len(left) > 0 and left[-1].isalpha():
            left = left[:-1]

        while len(right) > 0 and right[0].isalpha():
            right = right[1:]

        if left + word + right != input_string:
            result.append(left)
            result.append(f"({word})")
            result.append(right)
            result.append("\n")
    
    return ''.join(result)

if __name__ == "__main__":
    trie = load_trie()

    input_string = input("Enter the input string: ")
    clean_string = input_string.lower()
    found_words = []

    for i in range(len(clean_string)):
        print(clean_string[i], end="", flush=True)
        find_words_recursive(trie, clean_string[i], clean_string[i+1:], found_words, i, len(clean_string))
    
    found_words = list(set(found_words))  # Remove duplicates
    found_words.sort(key=lambda x: (len(x[0]), x[1]))  # Sort by length and then by start index
    print(f"Found words: {[(word, start, end) for word, start, end in found_words]}")

    replaced_text = replace_words_in_text(clean_string, found_words)
    print(f"Replaced text:\n{replaced_text}")
