class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # is the only problem if there is a cycle???
        """
        - build out a graph and then do bfs-style search, if we ever encounter a "seen" we're cooked
        - wait but no if 1301 is a prereq for 1331 and 1332 and then those are both prereqs for 2110 that's still fine
        - no they're directed edges it's fine
        """
        mapping = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            mapping[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if mapping[course] == []:
                return True
            visiting.add(course)
            for prereq in mapping[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            mapping[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
