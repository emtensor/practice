import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())

if n == 0: print(1)
else:
    arr = list(map(int, input().split()))

    if n == p and rank[-1] >= score:
        print(-1)
    else:
        rank = n + 1
        for i in range(n):
            if arr[i] <= score:
                result = i + 1
                break
        print(result)

