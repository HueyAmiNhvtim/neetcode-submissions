class TimeMap:

    def __init__(self):
        self.storage = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append(tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        l, r = 0, len(self.storage[key]) - 1
        max_prev_timestamp = self.storage[key][0][0]
        max_prev_timestamp_index = -1
        while l <= r:
            m = (l + r) // 2
            m_timestamp = self.storage[key][m][0]
            if m_timestamp == timestamp:
                return self.storage[key][m][1]
            if m_timestamp > timestamp:
                r = m - 1
            else: # If timestamp is bigger than middle
                if max_prev_timestamp <= m_timestamp:
                    max_prev_timestamp = m_timestamp
                    max_prev_timestamp_index = m
                l = m + 1

        if max_prev_timestamp_index != -1:
            return self.storage[key][max_prev_timestamp_index][1]
        else:
            return ""

        
