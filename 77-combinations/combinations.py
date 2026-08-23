class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(start, path):
            if len(path) == k:
                results.append(list(path))
                return

            for num in range(start, n + 1):
                if num in path:
                    continue
                
                path.append(num)
                dfs(num + 1, path)
                path.pop()

        dfs(1, [])
        return results
                