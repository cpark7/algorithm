
def move_cnt(now, target,n_list):
    cnt = 0
    if now == 0:
        now = 11
    if target == 0:
        target = 11

    check = [1,-1]
    if now in n_list:
        cnt =abs(target-now )//3
    else:
        if abs(target -now) == 1:
            cnt =1
        else:
            for i in range(2):
                if now +check[i] in n_list:
                    cnt = (abs(target - (now +check[i])) // 3 )+ 1
    return cnt
def solution(numbers, hand):
    answer = ''
    l_list = [1,4,7,10]
    r_list = [3,6,9,12]
    n_list = [2, 5, 8, 11]
    l_now = 10
    r_now = 12
    for num in numbers:
        print("r_now :" ,r_now ,"l_now :",l_now,"num :",num , answer)
        if num in l_list:
            l_now = num
            answer += 'L'
            continue
        elif num in r_list:
            r_now = num
            answer += 'R'
            continue
        else:
            l_move = move_cnt(l_now,num,n_list)
            r_move = move_cnt(r_now,num,n_list)
            if l_move >r_move :
                r_now = num
                answer+='R'
            elif l_move < r_move:
                l_now = num
                answer+='L'
            else:
                if hand == 'right':
                    r_now = num
                    answer+='R'
                else:
                    print("dksdhsl?")
                    l_now = num
                    answer+='L'
    return answer
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")