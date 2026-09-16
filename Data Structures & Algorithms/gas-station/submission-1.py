from typing import List
# You should aim for a solution with O(n) time and O(1) space, 
# where n is the size of the input array. 


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Get the difference between gas gained and cost at each gas index
        potential_gas = []
        
        for i in range(len(gas)):
            potential_gas.append(gas[i]-cost[i])
        print(f"potential_gas: {potential_gas}")
        # If gas_gained is negative, it is impossible to complete a trip no matter where we start
        if sum(potential_gas) < 0:
            return -1
        # Get the start of the maximum subarray.
        start_sa = 0
        cur_gas_gained = 0
        for i in range(len(potential_gas)):
            cur_gas_gained += potential_gas[i]
            if cur_gas_gained < 0:
                cur_gas_gained = 0
                start_sa = i+1

        return start_sa
