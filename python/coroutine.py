def total_coroutine():
    result=0
    try:
        while True:
            # yield : 이 코루틴을 수행하고자 할 때 넘겨주는 데이터를 받기 위한 문장, 여기서 대기
            x = (yield result) # yield + var 형태일때 next와 send 메서드의 리턴값으로 현재 var의 값을 return한다. 
            result = result + x
            # print('temporary result:',result)
    except Exception as e:
        print(e)
        
# 코루틴 인스턴스를 생성. 
# 함수내에 yield를 가지고 있다면 코루틴 인스턴스
co = total_coroutine()
print(next(co)) # yield를 만나기 전까지 실행
co.send(2)
print("im ironman")
co.send(5)
co.close()

# 함수와는 다르게 초기화되어 없어지지 않는다.
# 종료되지 않고 대기하도록, 무한루프를 사용한다.
# 강제로 종료하려면 코루틴 인스턴스가 close메서드를 호출하면 된다.
# 코루틴을 강제로 종료하면 generatorExit라는 error가 발생

# 코루틴은 일종의 인터럽트? => 인터럽트는 하드웨어적 개념이고 선점형 멀티테스킹
# 메모리는 어떻게 관리?
# 이벤트 루프에서 계속 작업중? => ㅇㅇ