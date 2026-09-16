# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        serialized = []
        visiting = deque()
        visiting.append(root)

        while visiting:
            node = visiting.popleft()
            if node:
                visiting.append(node.left)
                visiting.append(node.right)
                serialized.append(str(node.val))
            else:
                serialized.append("null")
        return "#".join(serialized)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_vals = data.split("#")
        if node_vals[0] == "null":
            return None
        queue = deque()
        root = TreeNode(int(node_vals[0]))
        queue.append(root)
        cur_index = 1 # Start at its children

        while queue:
            node = queue.popleft()
            if node_vals[cur_index] != "null":
                node.left = TreeNode(int(node_vals[cur_index]))
                queue.append(node.left)
            cur_index += 1 # Move to the right child
            if node_vals[cur_index] != "null":
                node.right = TreeNode(int(node_vals[cur_index]))
                queue.append(node.right)
            cur_index += 1
        return root
