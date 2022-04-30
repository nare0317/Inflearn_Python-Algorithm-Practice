import sys

sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int,input().split()))

# 평균
avg=int((sum(a)/n)+0.5) #반올림 하기 위해서, 평균에 0.5를 더한 뒤 정수형으로 바꿔줌
#avg=round(sum(a)/n) #주의! round 함수는 round_half_even방식 -> 4.5000 인경우 4로 나옴 

# 최소값
min=2147000000 # 정수의 최대값


for idx, x in enumerate(a): # enumerate -> idx 리스트의 인덱스값, x는 리스트값 
    diff=abs(x-avg) # 값 - 평균
    if diff<min:
        min=diff
        res=x
        res_idx=idx+1 #인덱스라 +1 해줘야함 

    # 평균과의 차이가 같은 수가 또 있는 경우
    elif diff==min:
        if x>res:   # >= 로 하면 같은 수인 경우, 뒤쪽 수를 출력하기 때문에 > 로 해줘야함. 
            res=x   #차이가 같은 경우, 더 큰 수를 출력
            res_idx=idx+1

