N = int(input())


for _ in range(N):
    pwd = input()
    left = []
    right = []
    for i in pwd:
        if i == '<':
            if left:
                element = left.pop()
                right.append(element)
        elif i == '>':
            if right:
                element = right.pop()
                left.append(element)
        elif i == '-':
            left.pop()
        else:
            left.append(i)

    left.extend(right)
    print(''.join(left))