

def solution(s):
    result = [] # 숫자들 담을 배열

    if len(s) == 1:
        return 1

    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        substr = s[:i]
        # abcdcdababcdcd
        for j in range(i, len(s)+i , i):
            if substr == s[j:j+i]:
                cnt += 1
            else:
                # 하나도 겹치는거 없으면
                if cnt == 1:
                    b = b + substr
                else:
                    b = b + str(cnt) + substr
                substr = s[j:j+i]
                cnt = 1
        result.append(len(b))

    return min(result)


def sol(s):
    answer = 0

    if len(s) == 1:
        return 1

    result = []

    for i in range(1, len(s)+1):
        newStr = ''
        cnt = 1
        subStr = s[:i]
        for j in range(i, len(s)+1, i):
            if subStr == s[j:j+i]:
                cnt += 1
            else: # 문자열을 만들어줌
                if cnt == 1:
                    newStr = newStr + subStr
                else:
                    newStr = newStr + str(cnt) + subStr
                subStr = s[j:j+i]
                cnt = 1
        print(newStr)
        result.append(len(newStr))

    return min(result)


print(sol("aabbaccc"))