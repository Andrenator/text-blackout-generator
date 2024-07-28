# trie.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def is_valid_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def find_words_with_prefix(self, prefix):
        def dfs(node, prefix):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child_node in node.children.items():
                dfs(child_node, prefix + char)
        
        node = self.root
        words = []
        for char in prefix:
            if char not in node.children:
                return words
            node = node.children[char]
        dfs(node, prefix)
        return words
