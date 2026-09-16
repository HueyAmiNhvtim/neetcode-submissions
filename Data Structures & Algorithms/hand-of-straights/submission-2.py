from typing import List
# You should aim for a solution as good or better than O(nlogn) time and
#  O(n) space, where n is the size of the input array. 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq_dict = dict()
        for val in hand:
                freq_dict[val] = freq_dict.get(val, 0) + 1

        for val in hand:
            if freq_dict[val] > 0:
                for i in range(val, val+groupSize):
                    if i not in freq_dict:
                        return False
                    freq_dict[i] -= 1
        return True

        