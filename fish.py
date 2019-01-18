from collections import deque
def solution(A, B):
    # write your code in Python 3.6
    d_stack = deque() # B[i] = 1
    u_stack = deque() # B[i] = 0
    
    for i in range(len(A)):
        if B[i] == 1:
            d_stack.append(A[i])
        else:
            flag = True # false when either 0 fish dies or 1 stack gets empty
            while flag:
                if len(d_stack) == 0:
                    flag = False
                    u_stack.append(0) # alive forever
                else:
                    s = d_stack.pop()
                    if s > A[i]:
                        # i dies
                        d_stack.append(s)
                        flag = False
                        # else:
                        # s dies
                        # already popped out

            
    return len(d_stack) + len(u_stack)
