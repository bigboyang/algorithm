def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop() 

result = []
n, m = map(int, input().split())
dfs()


# def dfs(idx):
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return
#
#     for i in range(idx, n+1):
#         if i not in result:
#             result.append(i)
#             dfs(i+1)
#             result.pop()
#
# result = []
# n, m = map(int, input().split())
# dfs(1)

# # n과m 4
# def dfs(idx):
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return
#
#     for i in range(idx, n+1):
#         result.append(i)
#         dfs(i)
#         result.pop()
#
# result = []
# n, m = map(int, input().split())
# dfs(1)

# n과m 5
# def dfs():
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return
#
#     for i in range(len(n_list)):
#         if not chk[i]: # 0번이면
#             chk[i] = 1
#             result.append(n_list[i])
#             dfs()
#             result.pop()
#             chk[i] = 0
#
# result = []
# # 1 7 8 9
# n, m = map(int, input().split())
# n_list = list(map(int, input().split()))
# chk = [0 for _ in range(n)] # chkedList
# n_list.sort()
# dfs()


# n과m 6
# def dfs(start):
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return
#
#     for i in range(start, n):
#         if not chk[i]:
#             chk[i] = 1
#             result.append(n_list[i])
#             dfs(i+1)
#             result.pop()
#             chk[i] = 0
#
# # 9 8 7 1
# result = []
# n,m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# chk = [ 0 for _ in range(n)]
# dfs(0)



# n과m 7
# def dfs():
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return
#
#     for i in range(n):
#         result.append(n_list[i])
#         dfs()
#         result.pop()
#
# # 9 8 7 1
# result = []
# n,m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# dfs()

# n과m 8
# def dfs(start):
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return
#
#     for i in range(start, n):
#         result.append(n_list[i])
#         dfs(i)
#         result.pop()
#
# # 9 8 7 1
# result = []
# n,m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# dfs(0)

# n과m 9
# def dfs(start):
#     if len(result) == m:
#         answer_before.append(' '.join(map(str, result)))
#         return
#
#     for i in range(start, n):
#         if not chk[i]:
#             chk[i] = 1
#             result.append(n_list[i])
#             dfs(start)
#             result.pop()
#             chk[i] = 0
#
# # 1 7 9 9
# result = []
# answer_before = []
# n,m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# chk = [0 for _ in range(n)]
# dfs(0)
#
# for x in sorted(list(set(answer_before))):
#     print(x)



# n과m 10
# def dfs(start):
#     if len(result) == m:
#         answer_before.append(' '.join(map(str, result)))
#         return
#
#     for i in range(start, n):
#         if not chk[i]:
#             chk[i] = 1
#             result.append(n_list[i])
#             dfs(i)
#             result.pop()
#             chk[i] = 0
#
# # 1 7 9 9
# result = []
# answer_before = []
# n,m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# chk = [0 for _ in range(n)]
# dfs(0)
#
# for x in sorted(list(set(answer_before))):
#     print(x)

# n과m 11
# def dfs(start):
#     if len(result) == m:
#         answer_before.append(' '.join(map(str, result)))
#         return
#
#     for i in range(start, n):
#             result.append(n_list[i])
#             dfs(start)
#             result.pop()
#
# # 1 7 9 9
# result = []
# answer_before = []
# n,m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()
# chk = [0 for _ in range(n)]
# dfs(0)
#
# for x in sorted(list(set(answer_before))):
#     print(x)


# n과m 12
def dfs(start):
    if len(result) == m:
        answer_before.append(' '.join(map(str, result)))
        return

    cur = 0
    for i in range(start, n):
        if cur != n_list[i]:
            cur = n_list[i]
            result.append(n_list[i])
            dfs(i)
            result.pop()

# 1 7 9 9
result = []
answer_before = []
n,m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
# chk = [0 for _ in range(n)]
dfs(0)
for x in answer_before:
    print(x)
