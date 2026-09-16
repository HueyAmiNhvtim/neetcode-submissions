class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq_dict = dict()
        for hand_val in hand:
            freq_dict[hand_val] = freq_dict.get(hand_val, 0) + 1
        
        for hand_val in hand:
            if freq_dict[hand_val] > 0:
                for i in range(hand_val, hand_val+groupSize):
                    if i not in freq_dict or freq_dict[i]==0:
                        return False
                    freq_dict[i] -= 1
        return True