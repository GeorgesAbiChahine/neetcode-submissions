from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        visited_pacific = set()
        visited_atlantic = set()

        # All cells touching each ocean
        pacific = []
        atlantic = []

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        def bfs(sources, visited):
            q = deque(sources)
            visited.update(sources)

            while q:
                ur, uc = q.popleft()

                for dr, dc in directions:
                    nr = ur + dr
                    nc = uc + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[ur][uc]):

                        visited.add((nr, nc))
                        q.append((nr, nc))

        # BFS from both oceans
        bfs(pacific, visited_pacific)
        bfs(atlantic, visited_atlantic)

        # Cells reachable from both oceans
        result = []

        for coord in visited_pacific:
            if coord in visited_atlantic:
                result.append(list(coord))

        return result