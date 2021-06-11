def solution(n,a,b):
    right = max(a,b)
    left = min(a,b)
    answer = 1
    while  (left % 2 == 0 or right - left != 1):
        left = (left+1)//2
        right = (right+1)//2
        answer+=1

    return answer
#        1
#    1       2
#  1   2   3   4
# 1 2 3 * 5 6 * 8

solution(16,8,7)