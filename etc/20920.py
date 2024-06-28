import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) < m: continue

    if word not in words: words[word] = 1
    else: words[word] += 1

words = sorted(words.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for word in words: print(word[0])

"""
1. dictionary�� Ư���� �ľ��ߴ�.
2. sorted()�� ������ �����ߴ�.
"""