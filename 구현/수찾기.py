N = int(input())
arr1 = map(int, input().split())
M = int(input())
arr2 = map(int, input().split())

idxs = [0]*M
mydict = dict(zip(arr1, idxs))

answer = [0]*M

for idx, data in  enumerate(arr2):
    if data in mydict.keys():
        mydict[data] += 1
        answer[idx] += 1

for i in answer:
    print(i)


