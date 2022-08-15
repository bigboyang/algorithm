from collections import defaultdict

def solution(k, dungeons):
    answer = 0

    dic = defaultdict(int)

    for dd in dungeons:
        dic[dd[0]] = [dd[1]/dd[0], dd[1]]

    sorted_dict = sorted(dic.items(), key=lambda item: item[1][0])

    for dun in sorted_dict:
        if k >= dun[0]:
            k -= dun[1][1]
            answer += 1

    return answer



print(solution(80,[[80,20],[50,40],[30,10]]))