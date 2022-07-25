from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] = []) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        visited = {node: Node(node.val, [])}
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in curr.neighbors:
                if neighbor in visited:
                    visited[curr].neighbors.append(visited[neighbor])
                else:
                    new_node = Node(neighbor.val, [])
                    visited[neighbor] = new_node
                    visited[curr].neighbors.append(new_node)
                    stack.append(neighbor)
        return visited[node]
