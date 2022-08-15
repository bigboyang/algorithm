

def solution(levels):

    Q = sum(levels)//4

    result = []

    for lev in levels:
        if lev > Q:
            result.append(lev)

    return min(result)


print(solution([1,2,3,4]))