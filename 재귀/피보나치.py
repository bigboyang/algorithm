n = int(input())

# 점화식은 재귀함수로 풀 수 있음

def fibo(n):
    if n == 0:
        return 0;
    if n == 1:
        return 1;
    return fibo(n-1) + fibo(n-2)

a, b = 0, 1
while n > 0:
    a,b = b, a+b
    n-=1

print(a)