from collections import Counter


def solution(N, stages):
    answer = []
    tmp = Counter(stages)
    res = len(stages)
    max_stage = N
    fail_list = []
    for stage in range(1, max_stage + 1):
        if stage not in stages:
            fail_list.append([stage, 0])
        else:
            if res:
                fail_list.append([stage, tmp[stage] / res])
        res -= tmp[stage]
    fail_list = sorted(fail_list, reverse=True, key=lambda x: (x[1], -x[0]))
    for x, y in fail_list:
        if x > max_stage:
            continue
        answer.append(x)

    return answer