'''
lru-cache란 ? least recently-used cache
=> 최근에 사용된 데이터를 저장하는 알고리즘

순서도
1. 데이터 접근
2. cache hit/miss 판단
3. hit일 경우 사용시간 갱신, 데이터 반환하고 종료
4. miss일 경우 cache size를 확인
    4-1.cache가 full이라면, 가장 오래전에 사용된 데이터를 현재 데이터로 교체
    4-2.cache가 사용 가능할 경우, 데이터를 저장
 
python package에서 제공하는 functools 라이브러리에 구현되어 있다. 직접 구현해보고 차이점 비교해보기
functools.lru_cache()
'''

import functools
@functools.lru_cache() # least recently used cache
def fibo_recursive(n):
    if n < 2:
        return 1
    else:
        return fibo_recursive(n-2) + fibo_recursive(n-1)
