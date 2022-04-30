import sys
#sys.stdin = open("input.txt", "rt")
'''
▶▶ K번째 수◀◀
2               --> 총 2개의 세트 
6 2 5 3         --> 6개의 숫자, 2-5번째 숫자 오름차순, 3번째로 작은 숫자 
5 2 7 3 8 9     --> [2,7,3,8] 오름차순 [2,3,7,8] 그 중 3번째 --> 7
15 3 10 3 
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
'''

T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split()) #처음 들어오는 숫자를 각각 변수에 담기
    a=list(map(int, input().split())) #다음으로 들어오는 숫자들을 공백으로 나눠서 list로 만듬
    a=a[s-1:e] #s번째부터 e번째까지의 수 
    a.sort() #정렬
    #print(a[k-1]) #k번째로 작은 수 (index라 -1) 
    print("#%d %d" %(t+1, a[k-1]))  #"#세트번호" 붙여주어 출력 
