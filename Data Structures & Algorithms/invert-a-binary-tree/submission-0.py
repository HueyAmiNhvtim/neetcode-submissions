# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        visited = deque()
        visited.appendleft(root)
        # DST to invert the tree. At each node, invert its children.
        while visited:
            node = visited.popleft()

            # Now do the inverting thing here
            tmp = node.left
            node.left = node.right
            node.right = tmp

            # Append the children node
            if node.left:
                visited.appendleft(node.left)
            if node.right:
                visited.appendleft(node.right)
        return root