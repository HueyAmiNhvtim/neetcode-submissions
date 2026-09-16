# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: {node.data} {dive node.left} {dive node.right}
        # inorder: {dive node.left} {node.data} {dive node.right}
        # ok...we know that the first element of preorder is the root node....
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        # We know that the first element of preorder is the root node.
        # And that preorder is just DFS
        root = TreeNode(preorder[0], None, None)
        mid = inorder.index(preorder[0]) # Find the index of the root node in the inorder traversal.
                                         # To the left of the root is its left subtree, the right its right subtree.
        # build the left subtree, we know that the elements up until mid are all part of the left subtree of root!
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # build the right subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # We know that the first element of the inorder list is the leftmost leaf.
        # At the root position in the inorder traversal array, every node to the left of it are members of the root's
        # left subtree, and every node to the right of it are members of the root's right subtree
        return root