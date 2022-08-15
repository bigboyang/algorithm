from collections import defaultdict
from math import ceil

def solution(tasks):
    answer = 0
    dic = defaultdict(int)
    # 동일 난이도 작업 개수
    for i in tasks:
        dic[i] += 1
    for key, val in dic.items():
        if val < 2: return -1
        answer += ceil(val / 3)
    return answer

print(solution([1,1,2,3,3,2,2]))