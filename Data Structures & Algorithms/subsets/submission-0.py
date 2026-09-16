class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Tree search....We know the state and the state transition, and we know how it works
        # But I have never done this before iteratively....
        # Let's go with DFS and treat this problem like a tree traversal problem
        results = []
        potential_subsets = deque()
        potential_subsets.appendleft(set())
        visited_subsets = []
        # Now how do you perform forward or arc consistency checking.....
        while potential_subsets:
            subset = potential_subsets.popleft()
            if subset not in visited_subsets:
                visited_subsets.append(subset)
                # Only add numbers that don't exist in the set.
                for i in range(len(nums)):
                    if nums[i] not in subset:
                        subset_list = list(subset)
                        subset_list.append(nums[i])
                        potential_subsets.appendleft(set(subset_list))

        return [list(mem) for mem in visited_subsets]