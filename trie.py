class Trie:
    def __init__(self):
        self.data = dict()
        islast = False 

    def insert(self, word):
        curr = self
        for i in word:
            if i not in curr.data:
                curr.data[i] = Trie()
            curr = curr.data[i]
        curr.islast = True

    def find(self,word):
        curr  = self
        for i in word:
            if i not in curr.data:
                return False
            curr = curr.data[i]
        return curr.islast


myTrie= Trie()
myTrie.insert("poo")
myTrie.insert("pop")
print(myTrie.find('poo'))
print(myTrie.find('popcorn'))
print type (myTrie)


