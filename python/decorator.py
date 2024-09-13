'''
Decorator
- aop의 개념
- 프로그램 공통 관심사항과 비지니스 로직을 분리
- 프록시 패턴
'''

# 함수 호출할때마다 얼마나 걸렸는지 계산하는 데코레이터
import datetime
def time_logging(func):
    def inner(*args):
        before = datetime.datetime.now()
        result = func(*args)
        after = datetime.datetime.now()
        print(f'running time is {after-before}')
        return result
    return inner

@time_logging
def test_func():
    lst=[i for i in range(100000)]
    return lst

@time_logging
def fibo(n):
    fibo=[1 for _ in range(n+1)]
    for i in range(2,n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]
    return fibo

#recursive하게 호출하는 함수의 경우 time_logging도 recursive하므로 다른 방법을 모색해야 한다.
@time_logging
def fibo_recursive(n):
    if n < 2:
        return 1
    else:
        return fibo_recursive(n-2) + fibo_recursive(n-1)

def time_logging_with_flag(func):
    # 로깅 플래그를 저장하는 속성 추가
    func._is_logging = False # > 함수는 객체이므로 동적으로 속성을 추가해주는 것이 가능하다.
    def inner(*args, **kwargs):
        if not func._is_logging:
            func._is_logging = True
            before = datetime.datetime.now()
            result = func(*args, **kwargs)
            after = datetime.datetime.now()
            print(f'running time is {after - before}')
            func._is_logging = False
            return result
        else:
            # 재귀 호출 시에는 단순히 함수만 호출
            return func(*args, **kwargs)
    return inner

@time_logging_with_flag
def fibo_recursive(n):
    if n < 2:
        return 1
    else:
        return fibo_recursive(n-2) + fibo_recursive(n-1)

# 혹은 제공하는 라이브러리를 사용이 가능하다.
import functools
@functools.lru_cache() # least recently used cache
@time_logging
def fibo_recursive(n):
    if n < 2:
        return 1
    else:
        return fibo_recursive(n-2) + fibo_recursive(n-1)

fibo(40000)
fibo_recursive(40)