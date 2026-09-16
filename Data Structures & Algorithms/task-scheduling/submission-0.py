class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        frequency = [-cnt for cnt in counter.values()] # Store all task that can be executed immediately, prioritizing
        # the most frequent ones at this time.
        heapq.heapify(frequency)

        task_queue = deque() # Store task + the min time they are gonna be available.
        time = 0
        while True:
            # If both frequency heap and task queue are empty, quit
            if not frequency and not task_queue:
                break

            # Increment time by 1
            time += 1
            # If the max heap is empty, that means no task can be executed at this moment => idle phase.
            if not frequency:
                # Accelerate time to the next available time in the queue (the "idle" phase)
                time = task_queue[0][1]
            else:
                # Execute the task and put it into the cooldown queue.
                cnt = 1 + heapq.heappop(frequency)
                if cnt:
                    task_queue.append([cnt, time+n])

            # If there is task in queue and the first available task can be executed at this time, add it back to the maxheap!
            if task_queue and task_queue[0][1] == time:
                heapq.heappush(frequency, task_queue.popleft()[0])

        return time