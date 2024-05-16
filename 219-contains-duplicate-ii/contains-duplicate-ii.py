class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value=set()
        l=0
        for r in range(len(nums)):
            if r-l > k:
                value.remove(nums[l])
                l+=1
            if nums[r] in value:
                return True
            value.add(nums[r])
        return False