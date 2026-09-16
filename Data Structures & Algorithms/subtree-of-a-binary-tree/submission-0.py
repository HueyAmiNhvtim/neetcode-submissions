# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        visiting_root = deque()
        # We going BFS instead (basically, at the same level, look for the node that matches the root of subRoot).
        # Then use DFS or BFS to perform same tree comparison at that node.

        visiting_root.append(root)

        while visiting_root:
            node = visiting_root.popleft()
            if node and node.val == subRoot.val:
                # Begin performing same_tree comparison via DFS
                visiting_tree = deque()
                visiting_tree.appendleft((node, subRoot))
                same_tree = True
                while visiting_tree:
                    root_node, subroot_node = visiting_tree.popleft()

                    if not root_node and not subroot_node:
                        continue
                    if not root_node or not subroot_node or root_node.val != subroot_node.val:
                        same_tree = False
                        break
                        
                    visiting_tree.appendleft((root_node.left, subroot_node.left))
                    visiting_tree.appendleft((root_node.right, subroot_node.right))
                if same_tree:
                    return same_tree
            if node and node.left:
                visiting_root.append(node.left)
            if node and node.right:
                visiting_root.append(node.right)
        return False