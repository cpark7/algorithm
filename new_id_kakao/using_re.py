import re
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^\w\.-]', '', st)
    st = re.sub('\.+', '..', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = "a" if not st else st[:15]
    st = re.sub('[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    print(st)
    return st


solution("bbbbbBASSDAXZ$^#$%#$%#$%@#$.asdasd...vasdfvfczv.[-a-as-df.sadfsadf")
