# 섹션2 - 8. 뒤집은 소수

import sys
sys.stdin=open("8. 뒤집은 소수/in1.txt","r")
n=int(input())  # 자연수 개수 
nums=list(map(int, input().split())) # n개의 자연수 

# 내 풀이 
""" 
def reverse(nums):
    '''
    배열의 숫자를 뒤집는 함수 
    '''
    reverse_nums=[]
    for i in range(0,n):
        x=nums[i]
        rem = 0
        res = 0
        while x>=1:
            rem=x%10
            x=x//10
            res=(res*10)+rem
        
        reverse_nums.append(res)

    return reverse_nums

reverse_nums = reverse(nums)
"""

#강사님 풀이 
def reverse(x):
    '''
    숫자를 뒤집는 함수 
    '''
    res=0
    while x>0:           
        rem=x%10        # x를 10으로 나눈 나머지
        res=res*10+rem  # res에 res*10을 곱한 뒤, x를 10으로 나눈 나머지를 더한 값을 넣어줌. 
        x=x//10         # x를 10으로 나눈 몫으로 변경 
    return res

"""
예를들어, 291인 경우 
rem=291%10=1  res=0*10+1=1      x=291//10=29
rem=29%10=9   res=1*10+9=19     x=29//10=2 
rem=2%10=2    res=19*10+2=192   x=2//10=0      -> break 
"""

def isPrime(x):
    '''
    소수인지 판별하는 함수 
    '''
    if x==1:                    # 1인경우, 소수가 아니기 때문에 False
        return False        
    for i in range(2,x//2+1):   # 2부터 시작해서 x의 반이 되는 지점까지만 반복하면 됨. (16이면, 2*8은 16이므로, 2,3,4,5,6,7,8까지 체크)
        if x%i==0:              # i로 나눠지는 경우 -> 소수가 아님. False
            return False
    else:                       # 아닌경우, True 리턴
        return True

# for else 문 : for문이 중간에 break나 return 등으로 끊기지 않고 끝까지 수행되었을 때 else 문을 수행

# 최종 결과 출력
for x in nums:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ') #옆으로 출력
