def solve(list,time):
    answer = 0
    n = len(list)
    m = len(list[0])
    cnt = 0
    """
    for i in range(time):
        for j in range(m):
            if list[-1-i][j] & 1 == 0:
                cnt+=1
    """
    i =0
    j=0
    cnt+= 1 if list[-(1+i)][j] & 1 == 0 else print(cnt)
    print(cnt)
    return answer



l = [[0,0,0,0,1,0],
     [1,1,1,1,0,1],
     [0,0,0,0,1,0],
     [1,1,0,0,0,1],
     [0,1,0,0,0,1]]

solve(l,2)