# 24.09.05 / 제로; Silver 4
# Baekjoon Online Judge: 10773
# Data Structure / Stack
import sys

K = int(sys.stdin.readline())
numbers = []
total = 0
for _ in range(K):
  number = int(sys.stdin.readline())
  if number == 0:
    total -= numbers.pop()
  else:
    total += number
    numbers.append(number)

print(total)