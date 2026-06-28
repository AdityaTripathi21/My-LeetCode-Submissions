from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            graph[p].append(c)
        
        visited = set()
        visiting = set()

        def has_cycle(course):
            if course in visiting:
                return True
            
            if course in visited:
                return False
        
            visiting.add(course)
            for c in graph[course]:
                if has_cycle(c):
                    return True

            visiting.remove(course)
            visited.add(course)

            return False

        for course in range(numCourses):
                if has_cycle(course):
                    return False
        return True


        
