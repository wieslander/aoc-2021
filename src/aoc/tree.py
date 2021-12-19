class BinaryTree:
    def __init__(self, left, right, value=None):
        self.left = left
        self.right = right
        self.value = value

    def is_leaf(self):
        return self.left is None and self.right is None

    def traverse_depth_first(self):
        depth = 0
        remaining = [(self, 0)]

        while remaining:
            node, depth = remaining.pop()
            yield node, depth

            depth += 1
            if node.right is not None:
                remaining.append((node.right, depth))
            if node.left is not None:
                remaining.append((node.left, depth))

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return f"({self.left}, {self.right})"
