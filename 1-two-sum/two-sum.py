class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, val in enumerate(nums):
            if target - val in dic:
                return [dic[target - val], i]
            dic[val] = i
