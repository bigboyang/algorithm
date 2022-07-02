n = int(input()) # 14

sec = 0 #
k = 1

while n != 0:
    if k > n:
        k = 1
    n -= k
    k += 1
    sec += 1

print(sec)