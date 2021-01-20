class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def charToIndex(self, ch):
        return ord(ch)-ord('a')
    
    def add(self, word):
        current = self.root
        for letter in word:
            index = ord(letter)-ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.end= True
    
    def search(self, word):
        current = self.root
        for letter in word:
            index = ord(letter)-ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.end


t= Trie()
t.add("hello")
t.add("pooja")
t.add("please")
print t.search("hello")
print t.search("chu")


class Node:
    def __init__(self):
        self.data = [None]*26
        self.isLast = False
class WordDictionary(object):

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        current = self.root
        for letter in word:
            index = ord(letter)-ord("a")
            if not current.data[index]:
                current.data[index] = Node()
            current = current.data[index]
        current.isLast = True
            
    def search(self, word):
        current = self.root
        for letter in word:
            index = ord(letter)-ord("a")
            print current.data[index], index
            if not current.data[index]:
                return False
            current = current.data[index]
        return current.isLast
t= WordDictionary()
t.addWord("hello")
t.addWord("pooja")
t.addWord("please")
print t.search("hello")
print t.search("chu")