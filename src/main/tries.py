class TrieNode:

    def __init__(self):
        self.chars = {}
        self.end_of_word = False

class Trie:
    # Initialize
    def __init__(self):
        self.header = TrieNode()

    # Insert word
    def insert(self, word: str):

        # Edge case
        if word == "":
            return "Dont give empty word"
        
        # Regular case
        # Initialize current node
        curr_node = self.header

        # Loop through all the charactes and start adding into the header
        for c in word:
            # Check if the character exists, if not add the Trie node
            if not c in curr_node.chars:
                # Setup the trie node
                curr_node.chars[c] = TrieNode()

            # Go next level in trie
            curr_node = curr_node.chars[c]
        
        # Last character set as end of word
        curr_node.end_of_word = True

        print(f"The word inserted")

    # Search word
    def search_word(self, word: str):
        # Edge case
        if word == "":
            return "Dont give empty word"
                
        # Regular
        # Loop through the characters for the trie tree
        curr_node = self.header
        for c in word:
            
            if c not in curr_node.chars:
                return False
            
            # Point to the next level
            curr_node = curr_node.chars[c]

        # End reached
        return curr_node.end_of_word

    # Search prefix
    def search_prefix(self, prefix: str):
        # Search for prefix
        # Edge case
        if prefix == "":
            return "Dont give empty word"
                
        # Regular
        # Loop through the characters for the trie tree
        curr_node = self.header
        for c in prefix:
            
            if c not in curr_node.chars:
                return False
            
            # Point to the next level
            curr_node = curr_node.chars[c]

        # End reached
        return True

    # Print trie
    def print(self):
        # Print an in order traversal of the tree:
        # Do an In order traversal

        # Edge case

        # For all Trie nodes, We will go deep and print each
        def _print(node: TrieNode):

            # Check all words
            for character in node.chars:                
                print(f"Char: {character}")

            # Edge case
            if node.end_of_word:
                return
            
            # Check all words
            for character in node.chars:                
                # Do downwards:
                _print(node.chars[character])

        _print(node=self.header)

if __name__ == "__main__":

    trie = Trie()
    trie.insert(word="apple")
    trie.insert(word="ape")

    # Positive
    given_word = "apple"
    print(f"Word apple is found : {trie.search_word(word=given_word)}")
    given_word = "ape"
    print(f"Word ape is found : {trie.search_word(word=given_word)}")

    # Negative
    given_word = "ale"
    print(f"Word ale is found : {trie.search_word(word=given_word)}")

    # Positive
    given_word = "app"
    print(f"Prefix app is found : {trie.search_prefix(prefix=given_word)}")
    given_word = "am"
    print(f"Prefix am is found : {trie.search_prefix(prefix=given_word)}")

    trie.print()
