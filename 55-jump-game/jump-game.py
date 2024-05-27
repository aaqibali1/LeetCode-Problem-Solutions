class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for jumps in nums:
            if max_jump < 0:
                return False
            max_jump = max(max_jump, jumps)
            max_jump -= 1
        return True