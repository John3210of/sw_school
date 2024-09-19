# copy
import copy
lst1=[1,2,3,4]

# shallow copy
lst2=copy.copy(lst1)
lst2[0]=1000
print(lst1) # [1, 2, 3, 4]
print(lst2) # [1000, 2, 3, 4]

lst3=[[1,2],[3,4]]
lst4=copy.copy(lst3)
lst4[0][0]=1000
# 재귀적으로 복제하지 않기 때문에 2차원 리스트의 경우 수정이 가능하다.
print(lst3) # [[1000, 2], [3, 4]]
print(lst4) # [[1000, 2], [3, 4]]

# deep copy 재귀적으로 복제
lst3=[[1,2],[3,4]]
lst4=copy.deepcopy(lst3)
lst4[0][0]=1000
# 재귀적으로 복제하기 때문에 수정이 불가능하다.
print(lst3) # [[1, 2], [3, 4]]
print(lst4) # [[1000, 2], [3, 4]]

# 약한 참조 소멸자 부르기
import weakref

class Temp:
    def __del__(self):
        print("인스턴스 del")

obj1=Temp()
# obj2=obj1
obj2=weakref.ref(obj1) # refcount를 증가시키지 않고 참조를 복사++obj1=None
print("program exit")