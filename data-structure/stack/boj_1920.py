# 24.09.03 / 수 찾기; Silver 4
# Baekjoon Online Judge: 1920
# Data Structure / Stack
import sys

N = int(sys.stdin.readline())
origin = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
comparison = list(map(int, sys.stdin.readline().split()))

for c in comparison:
  print(1 if c in origin else 0)


# Problem) list + in => 시간 초과 문제
# Solution) dictionary 이용 => 난잡한 코드
# Solution) set + in 이용
