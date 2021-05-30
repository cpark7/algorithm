def solution(n):
    answer = 0
    st = []
    calc = 1
    while n>0:
        st.append(n%3)
        n =  (n -(n%3))//3
    while st:
        answer+= st.pop()*calc
        calc*=3
    return answer

solution(45)