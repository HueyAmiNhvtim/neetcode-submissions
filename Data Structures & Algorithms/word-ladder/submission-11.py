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

        steps = float("inf")
        cur_state = deque()

        cur_state.appendleft((beginWord, 1))
        visited = set()
        target_found = False
        while cur_state:
            cur_word, cur_steps = cur_state.popleft()
            if cur_word == endWord:
                steps = min(steps, cur_steps)
                target_found = True
            else:
                # Loop through each letter in the current state
                for i in range(len(cur_word)):
                    cur_word_list = list(cur_word)
                    for char in legalCharSet:
                        # Prevent adding the same state to the state stack
                        if char != cur_word[i]:
                            cur_word_list[i] = char
                            next_word = "".join(cur_word_list)
                            if next_word not in visited and next_word in wordSet and cur_steps+1 < steps:
                                cur_state.appendleft((next_word, cur_steps + 1))
                                visited.add(next_word)
    

        if target_found:
            return steps
        else:
            return 0