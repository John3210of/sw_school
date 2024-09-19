class Abc:
    def __init__(self) -> None:
        pass
# 클래스에 존재하지 않아도, 동적할당이 가능하다.
a= Abc()
a._name="asdf"
print(a._name)

# 상호배제는 인스턴스/메서드 단위기 때문에 직접 접근하게 되면 상호배제를 적용하기가 어려운 경우가 많다.
# ⇒따라서 속성을 private로 숨기고, 메서드는 public으로 만든다.
class MyClass:
    def __init__(self, value):
        # 실제 값은 비공개 속성으로 설정.관례적으로 _ 를 붙여 표현한다.
        self._value = value

    @property
    def value(self):
        # Getter: _value 값을 반환
        return self._value
    
    @value.setter
    def value(self, new_value):
        # Setter: _value 값을 설정하면서 검증이나 로직 추가 가능
        if isinstance(new_value, int) and new_value > 0:
            self._value = new_value
        else:
            raise ValueError("Value must be a positive integer")

obj = MyClass(10)
print(obj._value)
obj.value = 20 
print(obj.value)


class SlotTest:
    __slots__ = ['name']
    def __init__(self):
        pass

a=SlotTest()
a.name='slotname'
print(a.name)
try:
    a.age=123
except Exception as e:
    print(e)

class InstanceTest:
    pass
ins1=InstanceTest()    
ins2=InstanceTest()    
print(ins1 is ins2) # False

class SingleTonTest:
    # return할 instance를 저장할 변수
    __instance = None # ?????
    
    # 없을때만 생성하도록
    def __new__(cls,*args,**kargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls,*args,**kargs)
        return cls.__instance

ins1=SingleTonTest()
ins2=SingleTonTest()
print(ins1 is ins2) # True

# 
class Person:
    def __init__(self):
        self.name = ''
        self.hobbies = []

    def getName(self):
        return self.name

    def getHobbies(self):
        return self.hobbies

    def getHobby(self,idx):
        return self.hobbies[idx]
    
    def setHobbies(self,hobbies):
        self.hobbies = hobbies
    
    def setHobby(self,idx,hobby):
        self.hobbies.insert(idx,hobby)
