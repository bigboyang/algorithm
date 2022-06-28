import copy


def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return

    array.append(" ")
    recursive(array, n)
    array.pop()

    array.append("+")
    recursive(array, n)
    array.pop()

    array.append("-")
    recursive(array, n)
    array.pop()


N = int(input())
for _ in range(N):
    operators_list = []
    num = int(input())
    recursive([], num-1)

    integers = [i for i in range(1, num+1)]

    for op in operators_list:
        string = ""
        for i in range(num -1):
            string += str(integers[i]) + op[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()






