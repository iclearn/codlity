from collections import deque

def solution(S):
    # write your code in Python 3.6
    open = ['(','[','{']
    d = {')':'(',']':'[','}':'{'}
    b_stack = deque()
    for i in range(len(S)):
        if S[i] in open:
            b_stack.append(S[i])
        else:
            try:
                item = b_stack.pop()
            except IndexError:
                return 0
            if item != d[S[i]]:
                return 0
    if len(b_stack) > 0:
        return 0
    return 1
