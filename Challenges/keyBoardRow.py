class KeyBoardRow:
    def findWords(self, words):
        
        wordList = []
        qw = "qwertyuiop"
        asd = "asdfghjkl"
        zx = "zxcvbnm"
        
        for i in words:
            j = i.lower()
            if len(set(qw).intersection(j)) == len(set(j)):
                wordList.append(i)
            
            elif len(set(asd).intersection(j)) == len(set(j)):
                wordList.append(i)
            
            elif len(set(zx).intersection(j)) == len(set(j)):
                wordList.append(i)
        
        return wordList

words = ["Hello","Alaska","Dad","Peace"]
_KeyBoardRow = KeyBoardRow()
print(_KeyBoardRow.findWords(words))