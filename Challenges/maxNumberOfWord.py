def maxNumberOfWord(text, brokenLetters):
        result = 0
        brokenLetter = set(brokenLetters)
        
        for i in text.split():
            if not (set(i).intersection(brokenLetter)):
                result = result + 1
        return result

text = "hello world"
brokenLetters = "ad"
print(maxNumberOfWord(text,brokenLetters))

text = "leet code"
brokenLetters = "lt"
print(maxNumberOfWord(text,brokenLetters))