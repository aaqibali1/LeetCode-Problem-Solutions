class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        i = 0
        j = 1
        l = len(words)-1
        while i < l:
            if j == len(words):
                i += 1
                j = i + 1
            if i < l and (words[j][:len(words[i])] == words[i]) and (words[j][-len(words[i]):] == words[i]):
                count += 1
            elif j == len(words):
                i += 1
                j = i
            j += 1
        
        return count