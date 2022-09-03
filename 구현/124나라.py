
def solution(n):

    dict = {1:1, 2:2, 0:4}

    arr = []
    # 41

    while n > 0:
        subfix = n % 3
        arr.append(str(dict[subfix]))
        if (subfix == 0):
            n -= 1
        n //= 3

    return ''.join(arr[::-1])


print(solution(10))