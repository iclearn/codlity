

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    s = []
    e = []
    for i in range(len(A)):
        s += [i-A[i]]
        e += [i+A[i]]
    # print(s)
    # print(e)
    s.sort()
    e.sort()
    
    # 0:s;1:e;2:both
    
    l = 2 * len(A)
    si = 0;ei = 0
    se = []
    for i in range(l):
        # print(si,ei)
        if si >= len(A):
            break
        if s[si] < e[ei]:
        	se += ['s']
        	si += 1
        elif s[si] > e[ei]:
        	se += ['e']
        	ei += 1
        else:
        	se += ['s']
        	si += 1
        	
    
    cur_circles = 0
    cur_intersections = 0
    
    # print(se)
    
    for i in range(len(se)):
        if se[i] == 's':
            cur_intersections += cur_circles
            if cur_intersections > 10000000:
                return -1
            cur_circles += 1
        elif se[i] == 'e':
            cur_circles -= 1
    

    return cur_intersections 


