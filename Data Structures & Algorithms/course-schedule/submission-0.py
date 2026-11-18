class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)

        visited = set()
        visiting = set()

        def dfs(a):
            if a in visiting:
                return False

            if a in visited:
                return True

            visiting.add(a)

            for v in adj[a]:
                if not dfs(v):
                    return False

            visiting.remove(a)
            visited.add(a)

            return True

        for v in range(numCourses):
            if not dfs(v):
                return False

        return True