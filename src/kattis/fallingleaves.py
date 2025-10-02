def fallingleaves(input_lines: list[str]) -> list[str]:
    def build_bst_and_preorder(tree_data):
        # Remove reversal, insert in input order
        root = None
        for level in tree_data:
            for ch in level:
                if root is None:
                    root = [ch, None, None]
                else:
                    curr = root
                    while True:
                        if ch < curr[0]:
                            if curr[1] is None:
                                curr[1] = [ch, None, None]
                                break
                            curr = curr[1]
                        else:
                            if curr[2] is None:
                                curr[2] = [ch, None, None]
                                break
                            curr = curr[2]

        # Preorder traversal
        stack = [root]
        result = ''
        while stack:
            node = stack.pop()
            if node:
                result += node[0]
                stack.append(node[2])  # Right child
                stack.append(node[1])  # Left child
        return result

    tree_data = []
    results = []

    for line in input_lines:
        if line == '$':
            if tree_data:
                results.append(build_bst_and_preorder(tree_data))
                tree_data = []
            break
        elif line == '*':
            results.append(build_bst_and_preorder(tree_data))
            tree_data = []
        else:
            tree_data.append(line)

    return results
