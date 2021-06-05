from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for menu_num in course:
        tmp = []
        for order in orders:
            combi = combinations(sorted(order), menu_num)
            tmp += combi
        check = Counter(tmp)
        if len(check) != 0 and max(check.values()) !=1 :
            answer +=["".join(f) for f in check if check[f] == max(check.values()) ]

    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])