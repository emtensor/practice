import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

print((1 + (w - 1) // (m + 1)) * (1 + (h - 1) // (n + 1)))

# print�� �ִ� ������ �����ϴ� ���� �߿��� ��