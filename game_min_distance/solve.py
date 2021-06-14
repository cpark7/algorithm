from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    real_map = [[-1] * (m+2) for _ in range(n+2)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    st = deque()
    """
    for i in range(n):
        for j in range(m):
            real_map[i+1][j+1] = maps[i][j]
    print(real_map)
    """
    real_map[1][1] = 1

    st.append([1,1])
    ## move 만들어. 완탐으 로 일단해보자
    while st:
        y,x = st.popleft()
        for i in range(4):
            if 1 <= x <=m and 1<= y <= n and maps[y-1][x-1] == 1:
                if real_map[y+dy[i]][x+dx[i]] == -1:
                    real_map[y+dy[i]][x+dx[i]] =real_map[y][x]+1
                    st.append([y+dy[i],x +dx[i]])
    answer = real_map[n][m]
    print(answer)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])