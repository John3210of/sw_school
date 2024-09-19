import time,threading

def run(id):
    for i in range(10):
        print(id)
        time.sleep(0.4)
run(1)
run(2)

# 스레드는 중간에 쉬는 시간이 생기면 다른 스레드로 제어권을 이동이 가능하다.
# 순서는 운영체제가 결정한다.

th1=threading.Thread(target=run,args=(1,))
th2=threading.Thread(target=run,args=(2,))
th1.start()
th2.start()

# thread를 만들기 위한 클래스, run메서드를 오버라이딩 하여 사용한다.
class ThreadTest(threading.Thread):
    def run(self):
        for i in range(10):
            print(self.getName())
            time.sleep(0.4)
th1=ThreadTest()
th2=ThreadTest()
th1.start()
th2.start()

# 상호배제 동시 수정 문제가 발생.
g_count=0
class ThreadTest(threading.Thread):
    def run(self):
        global g_count
        for i in range(10):
            print(self.name, '증가하기전',g_count)
            g_count+=1
            time.sleep(0.4)
            print(self.name, '증가후',g_count)
            time.sleep(0.4)
            
th1=ThreadTest()
th2=ThreadTest()
th1.start()
th2.start()

# Lock으로 문제를 해결, 공유자원을 수정하기 전에 Lock을 채우고 작업이 끝나면 반환
g_count=0
lock=threading.Lock()
class ThreadTest(threading.Thread):
    def run(self):
        global g_count
        global lock
        for _ in range(10):
            lock.acquire()
            print(self.name, '증가하기전',g_count)
            g_count+=1
            time.sleep(0.4)
            print(self.name, '증가후',g_count)
            time.sleep(0.4)
            lock.release()
th1=ThreadTest()
th2=ThreadTest()
th1.start()
th2.start()

'''
생산자와 소비자 문제
생산자가 공유자원을 생산, 소비자가 공유자원을 소비하는 경우
공유 자원을 생산하기 전에 공유자원을 소비하려고 하는 경우에 문제가 발생
공유자원이 없다면 기다리게 만들고 noti를 주어 재개하게 만든다.
'''
# 생산자와 소비자 문제를 해결하기 위한 인스턴스
cv = threading.Condition() 
sharedData=[]
# 꼭 global로만 사용해야 하는가?
# instance 선언시에 parameter로 cv instance를 받아서 처리하면 안되는이유가 있을까?
'''
class ThreadProducer(threading.Thread):
    def __init__(self, cv, sharedData):
        super().__init__()
        self.cv = cv
        self.sharedData = sharedData
    def run(self):
        ...
'''
class ThreadProducer(threading.Thread):
    def run(self):
        global cv
        global shareData
        for i in range(10):
            cv.acquire()
            
            print('data creating')
            sharedData.append(i)
            time.sleep(0.5)
            
            cv.notify() # 생산 noti를 보냄
            cv.release()

class ThreadConsumer(threading.Thread):
    def run(self):
        global shareData
        global cv
        for _ in range(10):
            cv.acquire()
            
            if len(sharedData) < 1: # 공유자원이 없으면 대기
                print('in waiting')
                cv.wait(5)
            print('data consuming')
            print(sharedData.pop())
            time.sleep(0.5)
            
            cv.release()

producer = ThreadProducer()
consumer = ThreadConsumer()
producer.start()
consumer.start()


# 세마포어
'''
공유자원의 개수가 여러개인 경우
공유자원의 개수가 0이 된 경우 waiting을 하게 만든다.
load balancer
사용법은 lock과 같은데, semaphore 클래스를 이용하고,
생성할 때 lock의 개수를 설정하는 것이 다르다.

동시에 수행되는 스레드의 개수는 cpu성능에 따라 다르게 설정
스레드에서 작업이 전환될때 자신의 정보를 저장하고 수행되는 스레드의 정보를 읽어오는 context switching이 발생
너무 많이 동작시키면 context switching 에 의한 오버헤드가 커지고, 이런것을 스레싱 thrashing 이라고 한다.
'''
# n개(3)까지 동시에 수행 가능
lock=threading.Semaphore(3)
class ThreadSema(threading.Thread):
    def run(self):
        lock.acquire()
        time.sleep(1)
        print(self.name)
        lock.release()

for _ in range(10):
    th=ThreadSema()
    th.start()