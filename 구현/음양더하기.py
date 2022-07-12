from collections import defaultdict

# [1,2,3]	[false,false,true]
absolutes = [1,2,3]
signs = ['false','false','true']

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


print(solution(absolutes, signs))