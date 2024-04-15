from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:  # Node 클래스 생성
    # 해시를 구성하는 노드 __init__
    
    def __init__(self,key:Any,value:Any,next:Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    #체인법으로 해시를 구현
    def __init__(self,capacity:int) -> None:
        self.capacity = capacity
        self.table = [None]*self.capacity
        
    def hash_value(self, key:Any) ->int:
        #해시값 구하는 함수
        if isinstance(key, int): # key값의 자료형이 int인지 검사
            return key%self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16)%self.capacity)
    
    def search(self,key:Any) ->Any:
        # 키가 key인 원소를 검색하여 값을 반환
        hash =self.hash_value(key)
        p = self.table[hash]
        
        while p is not None: #p가 None이 아닌경우에는 계속 while문 실행
            if p.key == key:
                return p.value
            p = p.next
            
        return None
    
    def add(self,key:Any,value:Any)->bool:
        #키가 key이고 값이 value인 원소를 추가
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return False
            p = p.next
            
        new_Node = Node(key,value,self.table[hash])
        self.table[hash] = new_Node
        
        return True
    
    def remove(self,key:Any) -> bool:
        # 키가 key인 원소를 삭제
        hash = self.hash_value(key)
        p = self.table[hash]
        p_front = None        
        while p is not None:
            if p.key == key:
                if p_front == None: # 자신이 제일 첫번째 노드인경우
                    self.table[hash] = p.next
                else:
                    p_front.next = p.next
                return True
            p_front = p
            p = p.next
        return False
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = "")
            while p is not None:
                print(f" -> {p.key}:{p.value}", end = "")
                p = p.next
            print()
            
                

            
                    