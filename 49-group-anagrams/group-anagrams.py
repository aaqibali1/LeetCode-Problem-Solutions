class Solution(object):
    def groupAnagrams(self, strs):
        res = collections.defaultdict(list) # O (1)

        for s in strs:
            count = [0] * 26 
            for c in s: 
                count[ord(c) - ord("a")] += 1 
            res[tuple(count)].append(s) # O (n)
        return res.values()