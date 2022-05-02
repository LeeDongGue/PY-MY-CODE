def fibo(n):
  if n <= 1:
    return n
  if memo[n] is None:
    memo[n] = fibo(n-2) + fibo(n-1)
  return memo[n]

n = int(input())
memo = [None] * (n + 1)
print(fibo(n))