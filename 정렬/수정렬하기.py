n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

# 선택정렬 : 낮은거부터 하나씩 앞으로

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if array[min_idx] > array[j]:
            min_idx = j
        array[i], array[min_idx] = array[min_idx], array[j]
for i in array:
    print(i)