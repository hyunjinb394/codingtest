# 1. 문제 이해
# 화폐 종류 n개로 합을 m으로 만들기

# 2. 문제 풀이
# 입력받은 수 중에서 가장 큰 수를 증가시키면서 합인 m으로 만들기

import sys
n, m  = map(int, sys.stdin.readline().strip())

array = []
for i in range(n):
    array.append(int(sys.stdin.readlines()))

d = [10001] * (m+1)

d[0] = 0
for i in range:
    for j in range(array[i], m+1):
        if d[j-array]