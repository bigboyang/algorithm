

def solution(price, money, count):
    answer = 0

    totalPrice = 0

    for m in range(count):
        totalPrice += price * (m+1)


    if totalPrice > money:
        answer = totalPrice - money

    return answer

# solution(3,20,4)
print(solution(3,20,4))