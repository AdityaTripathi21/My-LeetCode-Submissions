from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            graph[c].append(p)
        
        visiting = set()
        visited = set()
        res = []

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for p in graph[course]:
                if not dfs(p):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
            