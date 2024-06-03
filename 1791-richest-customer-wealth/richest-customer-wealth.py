class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for i in range(len(accounts)):
            add = sum(accounts[i])
            arr.append(add)
        maximum = max(arr)

        return  maximum