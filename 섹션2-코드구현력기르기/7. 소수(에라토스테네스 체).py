# 섹션2 - 7. 소수(에라토스테네스 체) 

import sys
sys.stdin=open("7. 소수(에라토스테네스 체)/input.txt","r")
n=int(input())  # 입력받은 정수 
ch=[0]*(n+1)    # 각 숫자가 소수인지 flag값을 넣을 배열  0 1 2 3 ... n+1 (0부터 시작이라 n+1만큼 만들어줌)
cnt=0           # 소수의 개수 



for i in range(2,n+1):
    if ch[i]==0:    # ch[i]==0이면 소수라는 뜻
        cnt+=1      # cnt를 1 증가 
        for j in range(i,n+1, i):   # i의 배수를 돌면서 
            ch[j]=1                 # ch 배열값을 1로 변경(=소수아님)

print(cnt)
