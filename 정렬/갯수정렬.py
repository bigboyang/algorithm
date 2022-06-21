# 인덱스를 값으로 보는 정렬법, 데이터가 등장한 횟수를 셈

import sys

n = int(sys.stdin.readline())
array = [0]*10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)