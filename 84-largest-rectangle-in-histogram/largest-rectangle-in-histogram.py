class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]

        
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                # print("index:{}, height {}, width {}, area {}".format(i,h,w,h*w)) -->
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


