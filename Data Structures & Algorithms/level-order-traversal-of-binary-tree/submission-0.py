# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        visiting = deque()
        visiting.append((root, 0))

        while visiting:
            node, level = visiting.popleft()
            if (level + 1) > len(result):
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.left:
                visiting.append((node.left, level+1))
            if node.right:
                visiting.append((node.right, level+1))

        return result