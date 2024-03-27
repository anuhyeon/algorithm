from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0 # 데이터가 저장되어있는 상태
    EMPTY = 1 # 버킷에 데이터가 비어있는 상태(버킷에 데이터가 들어온적이 없음)
    DELETE = 2 # 버킷에 데이터가 삭제된 상태
    
class Bucket:
    # 해시를 구성하는 버킷
    
    def __init__(self,key:Any=None,value:Any=None,stat: Status = Status.EMPTY) -> None: # 디폴트값 설정 (key = None , value = None, stat = Status.EMPTYT)
        #초기화
        self.key = key
        self.value = value
        self.stat = stat
        
    def set(self,key:Any,value:Any,stat:Status)->None:
        #모든 필드에 값을 설정 --> 변경가능
        self.key = key
        self.value = value
        self.stat = stat
        
    def set_status(self,stat:Status) -> None:
        #속성을 설정
        self.stat = stat
        
class OpenHash:
    #오픈주소법으로 구현하는 해시 클래스
    
    def __init__(self,capacity: int) -> None:
        #초기화
        self.capacity = capacity
        self.table = [Bucket()]*self.capacity # Bucket()인자에 아무것도 안들어갔으므로 디폴트 값인 None이랑 EMPTY가 들어가게됨
    
    def hash_value(self,key: Any) -> int:
        #해시값을 구함
        if isinstance(key,int):
            return key%self.capacity
        return(int(hashlib.md5(str(key).emcode()).hexdigst(),16)%self.capacity)
    
    def rehash_value(self,key:Any) -> int:
        #재해시값을 구함
        return (self.hash_value(key)+1) % self.capacity
    
    def search_node(self,key:Any) -> Any:
        #키가 key인 버킷을 검색
        hash = self.hash_value(key)
        bucket = self.table[hash]
        
        for i in range(self.capacity):
            if bucket.stat == Status.EMPTY:
                break
            elif bucket.stat == Status.OCCUPIED and bucket.key == key:
                return bucket
            
            hash = self.rehash_value(hash)
           #hash = self.rehash_value(key)  --> 매개 변수에 key를 넣으면 반복문 돌때마다 hash값이 바뀌지 않음 왜냐면 key 값이 변하지 않으니깐 그에 따른 reurn 값도 변하지 않게 됨.
            bucket = self.table[hash]

        return None
    
    def search(self,key:Any) -> Any:
        #키가 key인 원소를 검색하여 value를 반환
        bucket = self.search_node(key)
        if bucket is not None:
            return bucket.value # 검색에 성공하여 해당 value를 반환
        else:
            return None # 검색 실패 --> 해당 해시값을 가진 버킷이 비엇거나 없거나
        
    def add(self,key:Any,value:Any) -> bool:
        #키가 key이고 값이 value인 원소를 추가
        if self.search(key) is not None: # 이미 해당 테이블에 같은 키값이 등록되어있는 경우 중복등록인 경우 ///해시테이블엔 같은 키를 가지는 버킷은 없다 각각 키값은 하나씩
            return False     
        
        hash = self.hash_value(key)
        bucket = self.table[hash]
        
        for i in range(self.capacity):
            if bucket.stat == Status.EMPTY or bucket.stat == Status.DELETE:
                self.table[hash] = Bucket(key,value,Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            bucket = self.table[hash]
        return False
    
    def remove(self,key:Any) -> int:
        #키가 key인 원소를 삭제
        bucket  = self.search_node(key)
        if bucket is None:
            return False
        bucket.set_status(Status.DELETE)
        return True
    
    def dump(self) -> None:
        #해시테이블 출ㄹ력
        for i in range(self.capacity):
            print(f'{i:2}',end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key}({self.table[i].value})') 
            elif self.table[i].stat == Status.EMPTY:
                print('--미등록--')
            elif self.table[i].stat == Status.DELETE:
                print('--삭제완료--')       
       
        
            
            

        
        