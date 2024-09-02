# 24.09.02 / 괄호; Silver 4
# Baekjoon Online Judge: 9012
# Data Structure / Stack
import sys

def check_vps(ps):
    stack = []

    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return 'NO'
            stack.pop()

    if stack:
        return 'NO'
    
    return 'YES'

T = int(sys.stdin.readline())
for _ in range(T):
    ps = sys.stdin.readline().strip()
    print(check_vps(ps))

