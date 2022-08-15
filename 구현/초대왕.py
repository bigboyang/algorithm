from collections import defaultdict
from collections import Counter

def solution(invitationPairs):
    answer = []
    
    # 내가 초대 x10 , 내가 초대초대 x3 , 내가 초대초대초대 x1

    arr1 = []
    arr2 = []
    for i in invitationPairs:
        arr1.append(i[0])
    for i in invitationPairs:
        arr2.append(i[1])


    c1 = Counter(arr1)
    c2 = Counter(arr2)

    print(c1)
    print(c2)

    return answer




t = [
    [1,2],
    [2,3],
    [2,4],
    [2,5],
    [5,6],
    [5,7],
    [6,8],
    [2,9]
]

print(solution(t))