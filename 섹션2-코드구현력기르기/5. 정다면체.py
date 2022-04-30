# 챕터2 - 5.정다면체 

import sys 
sys.stdin = open("input.txt", "r")

n,m=map(int,input().split())

# 합의 개수를 담을 리스트
cnt=[0]*(n+m+3)     #더 넉넉하게 하려고 +3해줌.

# 최대값 
max=-2147000000     #가장 작은 값으로 초기화 

# 이중 for문 돌면서 cnt 배열 값을 더해줌 
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1

# cnt배열의 최대값 max에 담기 
for i in range(n+m+1):      # +1 해줘야 n+m까지 반복
    if cnt[i]>max:
        max=cnt[i]

# cnt배열 값이 max인 index 출력 
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
        