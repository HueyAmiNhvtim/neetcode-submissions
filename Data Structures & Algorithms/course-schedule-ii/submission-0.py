from collections import defaultdict

class Solution:
    # Topological sort, eh?
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Form dictionary, mapping course to the prerequisites
        course_to_prereq = defaultdict(list)
        
        for i in range(len(prerequisites)):
            pair = prerequisites[i]
            course_to_prereq[pair[0]].append(pair[1])

        # So the not all courses are included into the preprequisites huh?
        # So, how do you know where to start the chain of courses?
        # When a course has no prerequisites and can be added to result in any, any order!
        result = []

        # Use DFS, go as deep as possible. If there is a cycle, aka, when during DFS path, a node
        # is visited twice, return False the whole thing
        visited = set()
        included = set()

        for course in range(numCourses):
            if not course_to_prereq[course]:
                result.append(course)
                included.add(course)

        def dfs(course: int):
            if course in visited:
                return False
            visited.add(course)
            for prereq in course_to_prereq[course]:
                if not dfs(prereq):
                    return False
            # Mark node as visited
            course_to_prereq[course] = []
            visited.remove(course)  # Prevent cases when a node is in crossroad (aka, the node is visited twice
                                    # but on different paths)
            if course not in included:
                result.append(course) # Add the course to the result
                included.add(course)
            return True
        
        # For this, loop through 
        for i in range(numCourses):
            if not dfs(i):
                return []
        print(result)
        return result