# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.curr_index = 0
        self.in_order(root)
        print(self.arr)
        
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        self.arr.append(root.val)
        self.in_order(root.right)

    def next(self) -> int:
        val = self.arr[self.curr_index]
        self.curr_index+=1
        return val
        

    def hasNext(self) -> bool:
        return self.curr_index<=len(self.arr)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()