from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) ->  None: 
    pl = left
    pr = right
    # n = len(a)
    # x = a[n//2]
    x = a[(right + left)//2]
    
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if pr > left: qsort(a,left,pr)
    if pl < right: qsort(a,pl,right)
    
def quick_sort(a:MutableSequence) -> None:
    qsort(a,0,len(a)-1)

if __name__ == "__main__":
    print('퀵정렬을 수행합니다.')
    num = int(input("원소 수를 입력하시요: "))
    x = [None]*num # 원소수가 num인 배열을 생성
    
    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
    
    quick_sort(x)
    
    print("오름차순으로 정렬했습니다.")
    
    print(*x)