class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # All words in wordList are of same length, consisting of lowercase English letters, and are all distinct
        wordSet = set(wordList) 
        legalCharSet = set() 
        if endWord not in wordSet:
            return 0
        # Well, we have to know the legal steps we can make first.
        for word in wordList:
            legalCharSet = legalCharSet.union(set(list(word)))
        legalCharSet = list(legalCharSet)
        steps = float("inf")
        cur_state = deque()

        cur_state.appendleft((beginWord, 1))
        visited = set()
        target_found = False
        while cur_state:
            cur_word, cur_steps = cur_state.popleft()
            # For each letter, loop through all possible letters it can change to (representing a state transition)
            for i in range(len(cur_word)):
                cur_word_list = list(cur_word)
                for char in legalCharSet:
                    if char != cur_word[i]:
                        cur_word_list[i] = char
                        next_word = "".join(cur_word_list)
                        if next_word not in visited and next_word in wordSet and cur_steps+1 <= steps:
                            if next_word != endWord:    
                                cur_state.appendleft((next_word, cur_steps + 1))
                                visited.add(next_word)  # Prevent adding the same state to the state stack
                            else:
                                steps = min(steps, cur_steps + 1)
                                target_found = True

        if target_found:
            return steps
        else:
            return 0