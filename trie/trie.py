class TrieNode:

    def __init__(self):
        self.dict = {}
        self.is_end_node = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_string(self, string: str):
        current = self.root

        
        for char in string:
            if char not in current.dict:
                current.dict[char] = TrieNode()

            current = current.dict[char]

        current.is_end_node = True

    def contains(self, string: str) -> bool:
        current = self.root

        for char in string:
            if char not in current.dict:
                return False

            current = current.dict[char]

        return current.is_end_node


def test_trie():
    trie = Trie()

    trie.add_string('Existing String 1')
    trie.add_string('Existing String 2')

    assert trie.contains('Existing String 1') == True
    assert trie.contains('Existing String 2') == True
    assert trie.contains('Existing String 3') == False

