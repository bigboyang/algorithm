from collections import defaultdict


lottos = [0, 0, 0, 0, 0, 0]
win_nums= [38, 19, 20, 40, 15, 25]
def solution(lottos, win_nums):

    rank = defaultdict(int)

    rank[1] = 6
    rank[2] = 5
    rank[3] = 4
    rank[4] = 3
    rank[5] = 2
    rank[6] = 1

    correct = 0
    zero_cnt = 0

    for l in lottos:
        if l == 0:
            zero_cnt += 1
        if l in win_nums:
            correct += 1

    best = correct + zero_cnt
    worst = correct

    if (worst not in [6,5,4,3,2]):
        worst = 1
    if (best not in [6,5,4,3,2]):
        best = 1

    print(best)
    print(worst)

    answer = [rank[best], rank[worst]]
    return answer



print(solution(lottos, win_nums))