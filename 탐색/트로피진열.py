N = int(input())

def ascending(array):
    result = 1
    now = array[0]
    for i in range(1, len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result

array = []

for _ in range(N):
    array.append(int(input()))

# 오름차순으로 정렬


print(ascending(array))
array.reverse()
print(ascending(array))