class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        valMin, valMax = 1, 1
        for n in nums:
            if n == 0:
                valMin, valMax = 1, 1
                continue
            temp = n * valMax
            valMax = max(n * valMax, n * valMin, n)
            valMin = min(temp, n * valMin, n)
            res = max(res, valMax)
        return res