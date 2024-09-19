'''
객체 지향 언어에서는 상위 클래스 타입의 참조형 변수가 하위 클래스 타입의 참조를 저장할 수 있습니다.
-> 파이썬은 이런 제약이 약하다? 타입을 지정하지 않아서 다형성을 쉽게 구현하기 때문에

- 다형성이란?
Super:
    func first
Sub(Super):
    func first
    func second
    ,...

Super s = new Sub()
일때 s는 Super지만, Sub에서 정의된 다른것들은 사용 할 수 없다.
그렇다면 왜 굳이 이렇게 사용하는 것일까?

Star:
	attack

Protoss(Star):
	attack

Terran(Star):
	attack

Star s = new Star
Star t = new Terran

>> s.attack
>> t.attack
# 처럼 활용이 가능하다. 
# 메서드 이름은 같지만 실제로는 다르게 동작 할 수 있다. 
# 하지만 추상적 개념은 같으므로 가독성이 좋아진다.

파이썬의 경우는 타입지정을 하지 않기 때문에 제약이 약하게 보인다.
'''
# 상위 클래스 타입의 예외처리구문 예시
# 아래처럼 작성할 경우 Sub클래스의 예외로는 절대로 가지 않는다.
try:
    print(10/0) # zerodivisionerror occur
except BaseException as e:
    print(e)
    print('im in base') # -> 여기서 걸리게 됨. BaseException 은 ZeroDivisionError의 Super클래스
except ZeroDivisionError as e:
    print(e)
    print('im in zero')