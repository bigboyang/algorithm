N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(input())


row = [0]*N
col = [0]*M

for i in range(N):
    for j in range(M):
        if array[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count = 0
for i in range(N):
    if row[i] == 0:
        row_count += 1
col_count = 0
for i in range(M):
    if col[i] == 0:
        col_count += 1

print(max(row_count, col_count))



