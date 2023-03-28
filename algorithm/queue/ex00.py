# 기본
from collections import deque
queue = deque()
queue.append(1)
queue.append(6)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(9)
queue.append(8)
queue.popleft()
print('먼저 들어온 순서: ', queue)
queue.reverse()
print('나중 들어온 순서: ', queue)
