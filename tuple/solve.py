import re
def solution(s):
    answer = []
    d_list = s.split('}')
    set_list = []
    # making set_list
    for string in d_list:
        string = re.sub("\{+", "", string)
        string = re.sub("^[\,]", "", string)
        if string:
            set_list.append(string)
    # sort set_list by len
    set_list = sorted(set_list, key=lambda x: len(x))

    for a in set_list:
        # 숫자로 만들기
        tmp = a.split(",")
        for digit in tmp:
            if int(digit) not in answer:
                answer.append(int(digit))

    return answer
solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")