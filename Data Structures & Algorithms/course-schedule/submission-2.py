class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_to_prerequisite = defaultdict(list) # Map each node to its prerequisite
        for course, pre in prerequisites: # I think that numCourses = len(preprequisites)?
            node_to_prerequisite[course].append(pre)

        # So for [0, 1], [1, 0] the dict would look like: {1: 0, 0: 1}
        #                                                 {1: 0, 0: 2, 2:1} # also an invalid case
        # So, what would a valid course chain look like: {1:0, 0: 2, 2: 3, 3: 4}
        # Notice that there is no cycle here, and the chain ends when the value is not part of the dictionary key.
        # A cycle happens when the slow and fast pointer meets at the same point

        # Ya remember the slow and fast pointer thing? Of course, the prerequisites are not sorted. So you also
        # want to save a set of visited nodes too.
        visited = set()
        print(node_to_prerequisite)
        # ah damn.... a single course must be taken before you can take the other courses.... I see how it can be'
        # considered a graph problem now...
        def dfs(course_num):
            # Somehow we revisit the same course twice => Cycle detected
            if course_num in visited:
                return False
            if not node_to_prerequisite[course_num]:
                return True  # Course that are not a requirement, or has already been explored
            visited.add(course_num)
            for prerequisite in node_to_prerequisite[course_num]:
                if not dfs(prerequisite):
                    return False
            visited.remove(course_num)  # Path explored
            node_to_prerequisite[course_num] = []  # Confirmed to have no cycles, quit
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True