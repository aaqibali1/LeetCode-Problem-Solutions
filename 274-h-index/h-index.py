class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in non-decreasing order
        citations.sort()
        n = len(citations)
        
        # Iterate over the sorted citations
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        
        return 0