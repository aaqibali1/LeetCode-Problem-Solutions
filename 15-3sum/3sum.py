class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)-1):
            firstnum = nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                secnum = nums[j]
                thirdnum = nums[k]
                tosum = firstnum + secnum + thirdnum
                if tosum > 0:
                    k-=1
                elif tosum < 0:
                    j+=1
                else:
                    result.add((firstnum,secnum,thirdnum))
                    j+=1
                    k-=1
        return result