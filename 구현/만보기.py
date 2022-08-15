from itertools import chain

def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = []

    manbogi_one = {}
    manbogi_two = {}
    manbogi_three = {}
    n = len(steps_one)
    # 첫째 날
    for i in range(n):
        manbogi_one[names_one[i]] = steps_one[i]

    # 둘째 날
    n = len(steps_two)
    for i in range(n):
        manbogi_two[names_two[i]] = steps_two[i]

    # 셋째 날
    n = len(steps_three)
    for i in range(n):
        manbogi_three[names_three[i]] = steps_three[i]

    manbogi = {}
    for k, v in chain(manbogi_one.items(), manbogi_two.items(), manbogi_three.items()):
        if k not in manbogi:
            manbogi[k] = v
        else:
            manbogi[k] += v
    manbogi = sorted(manbogi.items(), key=lambda x : (-x[1], x[0]))
    answer = list(i[0] for i in manbogi)
    return answer