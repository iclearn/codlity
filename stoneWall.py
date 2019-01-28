from collections import deque

def solution(H):
    # write your code in Python 3.6
    d = deque()
    num_blocks = 1
    d.append(0)
    d.append(H[0])
    for h in range(1, len(H)):
        # print(h)
        while H[h] < d[-1]:
            d.pop()
        if d[-1] == 0:
            d.append(H[h])
            num_blocks += 1
        elif H[h] > d[-1]:
            d.append(H[h])
            num_blocks += 1
        # print(num_blocks)
            
    return num_blocks
