class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for num in nums:
            if num in check:
                return True
            else:
                check.add(num)