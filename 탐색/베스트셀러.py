N = int(input())

lib = {}

for _ in range(N):
    book = input()
    if book not in lib:
        lib[book] = 1
    else:
        lib[book] += 1

target = max(lib.values())
array = []

for book, number in lib.items():
    if number == target:
        array.append(book)

print(sorted(array[0]))

