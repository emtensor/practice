import sys
input = sys.stdin.readline

word = str(input().strip()).upper()
arr = [0] * 26
maxCnt = 0
maxChar = []

for i in word: 
    arr[ord(i) - 65] += 1

for i in range(26):
    if (arr[i] > maxCnt):
        maxCnt = arr[i]
        maxChar = [chr(i + 65)]
    elif (arr[i] == maxCnt):
        maxChar.append(chr(i + 65))

if (len(maxChar) == 1): print(maxChar[0])
else: print('?')

# ���ڿ�.count(����)�� ����ϸ� ���� ��
# count�� ����ϴ� ���� ������ �� �׷��� �𸣰���