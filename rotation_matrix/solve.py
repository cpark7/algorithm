from collections import deque
def rotation(query,matrix):

    st_y , st_x ,end_y ,end_x = query

    x_1 = deque(matrix[st_y-1][st_x-1:end_x])
    x_2 = deque(matrix[end_y-1][st_x-1:end_x])
    y_1 = deque()
    y_2 = deque()
    for i in range(st_y,end_y-1):
        y_1.append(matrix[i][st_x-1])
        y_2.append(matrix[i][end_x-1])
    if not y_1 or not y_2:
        x_1.appendleft(x_2.popleft())
        x_2.append(x_1.pop())
        total_min = min(list(map(min, x_1, x_2)))
    else:
        x_1.appendleft(y_1.popleft())
        y_2.appendleft(x_1.pop())
        x_2.append(y_2.pop())
        y_1.append(x_2.popleft())

    mini = min(x_1)
    mini = min(min(x_2),mini)
    if y_1:
        mini = min(min(y_1), mini)
        mini = min(min(y_2), mini)
    matrix[st_y-1][st_x-1:end_x] = list(x_1)
    matrix[end_y-1][st_x-1:end_x] = list(x_2)

    if y_1:
        for i in range(st_y,end_y):
            if y_1:
                matrix[i][st_x-1] = y_1.popleft()
                matrix[i][end_x-1] = y_2.popleft()
    print(query)
    print(matrix)
    return mini
def solution(rows, columns, queries):
    answer = []
    matrix = [[i*columns+j for j in range(1,columns+1)] for i in range(rows)]
    for query in queries:
        answer.append(rotation(query,matrix))

    print(answer)
    return answer

solution(	6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
