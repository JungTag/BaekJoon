import sys

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().split()]
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))