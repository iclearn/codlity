from collections import Counter

def solution(A):
    if len(A) == 0:
        return -1
    # write your code in Python 3.6
    e, f = Counter(A).most_common(1)[0]
    # print(e, f)
    if f > len(A)/2:
        return A.index(e)
        
    return -1

