def solution(s):
    answer = ''
    if len(s)%2 == 1:
        # 홀수면
        answer = s[len(s)//2]
    else:
        answer = s[len(s)//2 -1] + s[len(s)//2]
    return answer



# "abcde"
# "qwer"

print(solution("abcde"))