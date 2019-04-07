from collections import Counter
def solution(A):
    if len(A) == 1:
        return 0
    
    # write your code in Python 3.6
    e, f = Counter(A).most_common(1)[0]
    leaders = 0
    countE = 0
    
    for i in range(len(A)):
        if A[i] == e:
            countE += 1
        if countE > (i+1)/2 and (f-countE) > (len(A)-i-1)/2:
            leaders += 1
        # print(i, countE, leaders)
    return leaders
