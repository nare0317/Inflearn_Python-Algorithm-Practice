# 섹션2 - 6. 자릿수의 합 

import sys
sys.stdin=open("/Users/naraeim/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/6. 자릿수의 합/input.txt","r")
n=int(input())
a=list(map(int,input().split()))

# 각 자리수의 합을 구하는 함수 
def digit_sum(x):
    sum=0
    for i in str(x):    # x를 문자열로 바꿔서 한글자씩 돌며 반복
        sum+=int(i)     # int로 바꿔줘야함. 
    return sum

# def digit_sum(x):
#     sum=0
#     while x>0:
#         sum+=x%10       #125를 10으로 나눈 나머지 5 -> sum 
#         x=x//10         #125를 10으로 나눈 몫 12
#     return sum          #12를 10으로 나눈 나머지 2  -> sum 
#                         #12를 10으로 나눈 몫 1
#                         #1을 10으로 나눈 나머지 1  -> sum 
#                         #1을 10으로 나눈 몫 0 


# 최대값 담을 변수 
max=-2147000000

for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)


