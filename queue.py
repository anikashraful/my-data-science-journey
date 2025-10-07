# Queue (FIFO - first in, first out)

from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue
queue.popleft()

# output
print(queue)