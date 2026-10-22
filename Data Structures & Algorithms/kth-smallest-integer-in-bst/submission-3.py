# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visiting = deque()
        visiting.appendleft(root)

        # Yeah, this is just in-order traversal.... The question is...how do we know we reach the smallest element...
        # Yeah...how do we model recursive inorder traversal into the iterative equivalent...?
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visiting = deque()
        curr = root
        result = -1
        # Yeah, this is just in-order traversal.... The question is...how do we know we reach the smallest element...
        # Yeah...how do we model recursive inorder traversal into the iterative equivalent...?
        while visiting or curr:
            # At each node, go as left as possible
            while curr:
                visiting.appendleft(curr)
                curr = curr.left

            # The final added node is guaranteed to be in order.
            k -= 1
            curr = visiting.popleft()
            if k == 0:
                result = curr.val
                return result
            # Move to the right subtree
            curr = curr.right
        return result
        