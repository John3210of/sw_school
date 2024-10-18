# staticmethod
'''    
    함수 선언시에, @staticmethod를 명시
    > 독립적으로 사용 된다. 인스턴스가 없어도 호출이 가능하다.
    > 인스턴스와 상관 없는 어떤 행동을 하는 순수 함수를 만들 때 사용한다.
'''
# class StaticTest:
#     @staticmethod
#     def imstatic(num:int):
#         if num == 0:
#             return 1557
#         else:
#             return 1601
# a=StaticTest.imstatic(0)
# try:
#     assert(a==1557)
# except Exception as e:
#     print(e)

# class method
'''
    일반 메서드를 클래스 메서드로 변환시킴.
    @classmethod 를 사용한다.
    메서드는 self가 아닌 cls를 첫번째 인수로 받는다.
    1. 클래스 변수를 활용하여 클래스 수준의 로직을 정의하기도 한다.
    2. 팩토리 메서드의 역할도 할 수 있다.
'''
# 1.
class Product:
    tax_rate = 0.08
    
    @classmethod
    def update_tax_rate(cls,new_rate):
        cls.tax_rate = new_rate
    
    @classmethod
    def total_fee(cls,price):
        return price*(1+cls.tax_rate)
# 2.


# instance