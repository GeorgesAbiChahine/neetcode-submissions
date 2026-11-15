from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        source = Node(node.val)
        q = deque([node])
        visited = {node: source}

        while q:
            u = q.popleft()

            for nei in u.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)

                visited[u].neighbors.append(visited[nei])

        return source