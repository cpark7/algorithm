def solution(n, results):
    winner, loser = {}, {}
    for i in range(1, n+1):
        winner[i], loser[i] = set(), set()

    for i in range(1, n+1):
        for win, lose in results:
            if win == i:
                winner[i].add(win)
            if lose == i:
                loser[i].add(lose)
        for win in loser[i]:
            winner[win].update(winner[i])
        for lose in winner[i]:
            loser[lose].update(loser[i])
    cnt = 0
    for i in range(1, n+1):
        if len(winner[i]) + len(loser[i]) == n-1:
            cnt += 1
    return cnt

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])