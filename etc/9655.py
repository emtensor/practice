import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * (n + 1)

for i in range(2, n + 1):
    if (i > 3):
        if (arr[i - 3]): arr[i] = 0
        else: arr[i] = 1
    elif (i > 1):
        if (arr[i - 1]): arr[i] = 0
        else: arr[i] = 1

if (arr[n]): print('CY')
else: print('SK')

# dp�� ����϶�� �ǵ��� �˰�����, ����� Ȧ¦�� ���� �������� ���̶�� ������ ���.