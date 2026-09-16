# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        visiting = deque()
        visiting.appendleft(root)

        max_path_sum_so_far = dict() # Map node to a tuple consisting of the max path sum so far as that node,
                                     # and the max path sum if you don't allow splitting.
        max_path_sum_so_far[None] = (float("-inf"), float("-inf"))

        while visiting:
            node = visiting[0]
            if node.left and node.left not in max_path_sum_so_far:
                visiting.appendleft(node.left)
            elif node.right and node.right not in max_path_sum_so_far:
                visiting.appendleft(node.right)
            else:  # Only start processing once at the leaf or a node has all of its children processed
                node = visiting.popleft()
                left_split_sum, left_max_branch_sum = max_path_sum_so_far[node.left]
                right_split_sum, right_max_branch_sum = max_path_sum_so_far[node.right]

                split_sum = node.val + left_max_branch_sum + right_max_branch_sum
                max_branch_sum = node.val + max(left_max_branch_sum, right_max_branch_sum, 0)

                max_path_sum_so_far[node] = (split_sum, max_branch_sum)

                if (max_path_sum := max(split_sum, max_branch_sum)) > result:
                    result = max_path_sum

        return result