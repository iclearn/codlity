# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    s = []
    e = []
    for i in range(len(A)):
        s += [i-A[i]]
        e += [i+A[i]]
    print(s)
    print(e)
    s.sort()
    e.sort()
    
    cur_circles = 0
    cur_intersections = 0
    
    # 0:s;1:e;2:both
    
    l = 2 * len(A)
    si = 0;ei = 0
    for i in range(l):
        print(si,ei)
        if si >= len(A):
            break
        if s[si] < e[ei]:
            cur_intersections+=cur_circles
            cur_circles+=1
            si+=1
        elif s[si] > e[ei]:
            cur_circles-=1
            ei+=1
        else:
            cur_intersections+=cur_circles
            si+=1
            ei+=1
    # if s[0] == e[0]:
    #     cur_intersections += 1
    return cur_intersections 
        
