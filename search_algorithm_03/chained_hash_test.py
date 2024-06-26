from algorithm.search_algorithm_03.chained_hash import ChainedHash, Node
from enum import Enum

Menu = Enum('Menu',['추가','삭제','검색','덤프','종료']) # Menu라는 객체를 찍어낸 것, Enum의 첫번째 인자는 타입을 지정해주는 인자 
# for m in Menu:
#     print(m.value, m.name, Menu(1))

def select_menu() -> Menu:
    #메뉴 선택
    s = [f'({m.value}){m.name} ' for m in Menu]
    while True:
        print(*s, sep = "   ", end="")
        n = int(input(" : "))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
hash = ChainedHash(13)

while True:
    menu = select_menu()
    
    if menu == Menu.추가:
        key = int(input("추가할 키를 입력하세요 : "))
        value = input('추가할 값을 입력하시오 : ')
        # hash.add(key,value)
        if not hash.add(key,value): # 조건문에 넣어도 함수 실행됨. 헷갈리지 말것
            print("추가를 실패 하였습니다.")
    elif menu == Menu.삭제:
        key = int(input("삭제할 키를 입력하세요 : "))
        # hash.remove(key)
        if not hash.remove(key): # 조건문에 넣어도 함수 실행됨. 헷갈리지 말것
            print("삭제를 실패 하였습니다.")
    elif menu == Menu.검색:
        key = int(input("검색할 키를 입력하세요 : "))
        t = hash.search(key)
        if t is not None:
            print(f"검색한 키를 갖는 값은 {hash.search(key)} 입니다.")
        else:
            print('검색할 데이터가 없습니다.')
    elif menu == Menu.덤프:
        hash.dump()
    else:
        break
        
    
        
    