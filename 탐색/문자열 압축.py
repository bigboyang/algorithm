

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
            print(len(s)+i)
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




print(solution("ababcdcdababcdcd"))