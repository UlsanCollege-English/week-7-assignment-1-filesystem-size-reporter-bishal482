# src/filesystem.py

from collections import deque

class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []

    def __repr__(self):
        return f"Node({self.name!r}, {self.size}, children={len(self.children)})"


def total_size(node):
    """Return total file size of a node (including all descendants)."""
    if node is None:
        return 0
    # if it's a file (no children), return its size
    if not node.children:
        return node.size
    # folder: sum own size + all children
    return node.size + sum(total_size(child) for child in node.children)


def folder_sizes(node):
    """Return {folder_name: total_size} for all folders (not files)."""
    sizes = {}
    if node is None:
        return sizes

    def dfs(n):
        if not n.children:
            return n.size
        total = n.size
        for c in n.children:
            total += dfs(c)
        sizes[n.name] = total
        return total

    dfs(node)
    return sizes


def level_order(node):
    """Return list of levels (each a list of node names)."""
    if node is None:
        return []

    result = []
    q = deque([node])

    while q:
        level_len = len(q)
        level = []
        for _ in range(level_len):
            cur = q.popleft()
            level.append(cur.name)
            q.extend(cur.children)
        result.append(level)

    return result
