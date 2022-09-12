


def solution(array, commands):

    answers = []

    for cmd in commands:
        newArr = array[cmd[0]-1:cmd[1]]
        newArr.sort()
        answers.append(newArr[cmd[2]-1])
    return answers


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

