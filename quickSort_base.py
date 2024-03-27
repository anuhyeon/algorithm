from typing import MutableSequence

def partition(a : MutableSequence) -> None:
    n = len(a) # 들어온 MutbleSequence객체 a(리스트나 배열 등)의 크기(길이) 파악
    pl = 0 # pl이란 객체(a)의 제일 첫번째 인덱스(제일 왼쪽 인덱스)
    pr = n - 1 # pr이란 객체(a)의 제일 마지막 인덱스(제일 오른쪽 인덱스)9
    
    pivot = a[n//2] # 피봇은 a의 가운데 원소
    
    ##배열 a를 pivot으로 나누기
    while pl <= pr:
        while a[pl] < pivot : pl += 1
        while a[pr] > pivot : pr -= 1
        #if pl <= pr : # 이건 왜 쓴거지??
        a[pl], a[pr] = a[pr], a[pl]
        print(*a)
        pl += 1
        pr -= 1
        
    print('피벗 이하 그룹 : ', *a[0:pl])
    if pl > pr + 1:
        print('피벗인 그룹 : ', *a[pr+1:pl])
    print('피벗 이상 그룹 : ', *a[pr+1 : n])
        
    
 
if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소의 수를 입력하시오. :'))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    partition(x)    


    
    
    