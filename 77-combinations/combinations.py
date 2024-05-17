class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        for i in range(1,n+1):
            answer.append(i)
        return combinations(answer,k)