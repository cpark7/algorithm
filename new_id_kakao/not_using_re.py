def solution(new_id):
    sp = ['-', '_', '.']
    # 1단계
    new_id = new_id.lower()
    # 2단계 특문 제거
    length = len(new_id)
    new_id = list(new_id)

    for i in range(length):
        if new_id[i] not in sp and not new_id[i].isalnum():
            new_id[i] = ""
    new_id = "".join(new_id)
    #3단계 . 중복제거
    length = len(new_id)
    new_id = list(new_id)

    for i in range(length):
        if new_id[i] =='.':
            j = 1
            while(i+j < length and new_id[i+j] == "."):
                new_id[i+j] = ""
                j += 1
    new_id = "".join(new_id)

    #4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    #5단계
    if not new_id:
        new_id = "a"
    #6단계
    if len(new_id) >=16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    #7단계
    while(len(new_id) <=2):
        new_id+=new_id[-1]
    return new_id
