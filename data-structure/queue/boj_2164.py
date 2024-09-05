# 24.09.05 / 카드2; Silver 4
# Baekjoon Online Judge: 2164
# Data Structure / Queue
import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque(range(1, N+1))
for _ in range(N - 1):
  queue.popleft()
  queue.rotate(-1)

print(*queue)