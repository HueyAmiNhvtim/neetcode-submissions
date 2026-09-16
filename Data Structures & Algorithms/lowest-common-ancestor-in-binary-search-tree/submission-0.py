# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visiting = deque()
        visiting.appendleft(root)

        parent = dict()
        parent[root] = (root, 0)

        p_equiv, q_equiv = None, None

        # So for each children, record their parent and the current level, so that when we reach p and q, we can use the dictionary
        # to dive back up until a point where p and q paths overlap!
        while visiting:
            if p_equiv in parent and q_equiv in parent:
                break
            node = visiting.popleft()
            if node.val == p.val:
                p_equiv = node
            elif node.val == q.val:
                q_equiv = node

            _, node_level = parent[node]

            if node.left:
                parent[node.left] = (node, node_level + 1)
                visiting.appendleft(node.left)
            if node.right:
                parent[node.right] = (node, node_level + 1)
                visiting.appendleft(node.right)

        # Dive back
        ancestors = dict()
        _, p_level = parent[p_equiv]
        _, q_level = parent[q_equiv]
        ancestors[p] = p_equiv
        ancestors[q] = q_equiv

        if p_level < q_level:
            while p_level < q_level:
                ancestors[q], _ = parent[ancestors[q]]
                q_level -= 1
        elif q_level < p_level:
            while q_level < p_level:
                ancestors[p], _ = parent[ancestors[p]]
                p_level -= 1

        # Rely on the fact that a node in a BST has only 1 parent
        while ancestors[p] != ancestors[q]:
            # p is at a deeper level than p, diving back
            ancestors[p], _ = parent[ancestors[p]]
            ancestors[q], _ = parent[ancestors[q]]
            # How do you actually dive back... because p and q can have the same parent...in which case
            # the above while loop immediately exits

            # p and q can be on the same level but not share a parent...in which case advancing to the most common
            # ancestor is a matter of incrementing both things at a time...

            # Now...when p and q are not on the same level... STORE THE LEVEL when diving down.
            # Then whoever level is lower...dive back until level is equal to the level of the otherside,
            # Then both just got dove back until matching the same ancestor!

        return ancestors[p]
