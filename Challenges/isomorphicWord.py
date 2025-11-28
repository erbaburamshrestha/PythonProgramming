def isIsomorphic(s, t):
        wordDict = {}
        
        for i in range(len(s)):
            if s[i] not in wordDict.keys():
                if t[i] not in wordDict.values():
                    wordDict[s[i]] = t[i]
                else:
                    return False
            else:
                if wordDict[s[i]] != t[i]:
                    return False
        
        return True
s = "egg"
t = "add"
print(isIsomorphic(s,t))
s = "foo"
t = "bar"
print(isIsomorphic(s,t))