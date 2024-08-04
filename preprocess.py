import os
import re

def load_wordlist(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return set(f.read().split())

def save_wordlist(filepath, wordlist):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(wordlist)))

def clean_and_filter_words(text, wordlist):
    words = re.findall(r"\b[\w'-]+\b", text.lower())
    return set(words) - wordlist

def preprocess_files(data_directory):
    wordlist_path_original = os.path.join(data_directory, 'wordlist-original.txt')
    wordlist_path = os.path.join(data_directory, 'wordlist.txt')
    added_list_path = os.path.join(data_directory, 'added-list.txt')
    blacklist_path = os.path.join(data_directory, 'blacklist.txt')

    # Load existing wordlist and blacklist
    wordlist = load_wordlist(wordlist_path_original)
    blacklist = load_wordlist(blacklist_path)

    # Process added-list.txt
    with open(added_list_path, 'r', encoding='utf-8') as f:
        added_list_text = f.read()

    cleaned_added_list = clean_and_filter_words(added_list_text, wordlist)
    
    # Remove blacklist words from wordlist and cleaned_added_list
    wordlist -= blacklist
    cleaned_added_list -= blacklist

    # Save the updated word lists
    save_wordlist(wordlist_path, wordlist)
    save_wordlist(added_list_path, cleaned_added_list)

if __name__ == "__main__":
    data_directory = os.path.join(os.path.dirname(__file__), 'data')
    preprocess_files(data_directory)
