class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)
    return result


def is_bst(node, min_value=float("-inf"), max_value=float("inf")):
    if node is None:
        return True
    if not (min_value < node.value < max_value):
        return False
    return (
        is_bst(node.left, min_value, node.value)
        and is_bst(node.right, node.value, max_value)
    )


def check(name, root):
    values = inorder(root)
    print(f"[{name}] 中間順で並べると: {values}")
    print(f"[{name}] 2分探索木か？ -> {is_bst(root)}")
    print()


valid_tree = Node(
    17,
    left=Node(14, left=Node(10), right=Node(16)),
    right=Node(19, left=Node(18)),
)

invalid_tree = Node(
    15,
    left=Node(14, left=Node(10), right=Node(16)),
    right=Node(19),
)

check("2分探索木の条件を満たす木", valid_tree)
check("条件を満たさない木", invalid_tree)
