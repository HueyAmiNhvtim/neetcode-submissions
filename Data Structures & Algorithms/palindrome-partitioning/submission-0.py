from collections import deque
from typing import List


# You should aim for a solution with O(n * (2^n)) time and O(n) space, 
# where n is the length of the input string. 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        result = []
        potential_palindrome = deque()
        # Now, what are the initial states and state transition steps?
        # The intial state would be the first letter.
        # What information state that should be retained we will
        # think about it later...
        potential_palindrome.appendleft(([s[0]], 1))

        while potential_palindrome:
            pot_res, next_index = potential_palindrome.popleft()
            last_palindrome_check = self.check_palindrome(pot_res[-1])
            # The current latest substring is assumed to be the 
            # stepper. Either complete its role (and move on
            # to create a new substring) or add more characters
            # with the assumption that the end result is guaranteed
            # to be a palindrome
            
 
            if next_index == len(s):
                if last_palindrome_check:
                    result.append(pot_res)
            else:
                # Move on to create a new substring provided the following
                # conditions are met:
                #   1. there are letters left to be chosen
                #   2. the latest substring is guaranteed to be a palindrome
                if last_palindrome_check: # Implicit next_index < len(s)
                    potential_palindrome.appendleft((pot_res + [s[next_index]], next_index+1))
                
                pot_res[-1] = pot_res[-1] + s[next_index]
                potential_palindrome.appendleft((pot_res, next_index+1))
        
        return result


    def check_palindrome(self, s: str):
        # Do you remember the 2-pointer method?
        l, r = 0, len(s)-1
        while l < r: 
            if s[l] != s[r]:
                return False
            # There's no need to check for non-alphanumeric characters 
            # due to the given constraints
            l += 1
            r -= 1
        return True


