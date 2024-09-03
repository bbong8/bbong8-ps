# 24.09.03 / 스택; Silver 4
# Baekjoon Online Judge: 10828
# Data Structure / Stack
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
  operator = sys.stdin.readline().rstrip().split()

  if operator[0] == 'push':
    stack.append(int(operator[1]))
  elif operator[0] == 'pop':
    print(stack.pop() if stack else -1)
  elif operator[0] == 'size':
    print(len(stack))
  elif operator[0] == 'empty':
    print(0 if stack else 1)
  elif operator[0] == 'top':
    print(stack[-1] if stack else -1)
  else:
    print('Operator Error')


# 파이썬의 삼항연산자
# a ? b : c (x)
# b if a else c (o)