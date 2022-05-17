N = int(input())
n_list = []
count = 1
result = []
stack = []
# 4 3 6 8 7 5 2 1

for i in range(N):
    data = int(input())
    while count <= data:
        result.append('+')
        stack.append(count)
        count += 1
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)


print(result)

