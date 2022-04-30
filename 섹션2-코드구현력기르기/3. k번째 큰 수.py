import sys
#sys.stdin = open("input.txt", "rt")
'''
▶▶ 2-3. K번째 큰 수◀◀
1-100까지의 자연수가 적힌 n장의 카드 (같은 숫자 존재) 
이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록 
기록한 값 중 k번째로 큰 수를 출력하시오. 

10 3                            --> 10개의 숫자 중 3번째로 큰 수 
13 15 34 23 45 65 33 11 26 42
'''

n, k = map(int, input().split())    #첫줄 : 2개의 숫자
a = list(map(int, input().split())) #둘째줄 : 숫자리스트 
res=set()                           #set이라는 자료구조 : 중복을 제거한다. 

#3중for문 
for i in range(n):                  # i j m 
    for j in range(i+1, n):         # 1 2 3 4 5
        for m in range(j+1, n):     # 1 2 3 / 1 2 4 / 1 2 5 

            res.add(a[i]+a[j]+a[m]) # 중복을 제거하면서 합을 추가 (set은 append가 아니라 add!)


#print(res)
res=list(res) #set은 sort기능x --> list로 바꿔줌 'set' object has no attribute 'sort'
res.sort(reverse=True) #내림차순 정렬
#print(res)

print(res[k-1]) #k번째 
