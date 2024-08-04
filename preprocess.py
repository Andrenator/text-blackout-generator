import os
import re

def load_wordlist(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return set(f.read().split())

def save_wordlist(filepath, wordlist):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(wordlist)))

def clean_words(text):
    words = re.findall(r"\b[\w'-]+\b", text.lower())
    return set(words)

def preprocess_files(data_directory):
    wordlist_path_original = os.path.join(data_directory, 'wordlist-original.txt')
    wordlist_path = os.path.join(data_directory, 'wordlist.txt')
    added_list_path = os.path.join(data_directory, 'added-list.txt')
    blacklist_path = os.path.join(data_directory, 'blacklist.txt')

    # Load existing wordlist
    wordlist = load_wordlist(wordlist_path_original)

    # Process blacklist.txt
    with open(blacklist_path, 'r', encoding='utf-8') as f:
        blacklist_text = f.read()

    cleaned_blacklist = clean_words(blacklist_text)

    # Process added-list.txt
    with open(added_list_path, 'r', encoding='utf-8') as f:
        added_list_text = f.read()

    cleaned_added_list = clean_words(added_list_text)

    # Remove blacklist words from wordlist and cleaned_added_list
    wordlist = {word for word in wordlist if word not in cleaned_blacklist}
    cleaned_added_list = {word for word in cleaned_added_list if word not in cleaned_blacklist and word not in wordlist}

    # Save the updated word lists
    save_wordlist(wordlist_path, wordlist)
    save_wordlist(blacklist_path, cleaned_blacklist)
    save_wordlist(added_list_path, cleaned_added_list)

if __name__ == "__main__":
    data_directory = os.path.join(os.path.dirname(__file__), 'data')
    preprocess_files(data_directory)
