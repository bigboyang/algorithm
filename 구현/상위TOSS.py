

def solution(levels):
    answer = -1
    length = len(levels)
    i = 0

    while i < length-2:
        nums = levels[i:i+3]
        sums = sum(list(map(int, nums)))

        if sums == int(levels[i])*3:
            i += 3
            answer = max(answer, int(nums))
        else:
            i += 1
    return answer




print(solution([1,2,3,4,5,6,7,8,9]))