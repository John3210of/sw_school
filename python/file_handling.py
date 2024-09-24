with open('./test.bin','wb') as f:
    # encode string to byte
    f.write('hello 바이트'.encode())
    
with open('./test.bin','rb') as f:
    bytearray=f.read()
    print(bytearray)    # 웹에서 ajax로 데이터를 받고 바로 출력하면 이 형태로 보임
                        # b'hello \xeb\xb0\x94\xec\x9d\xb4\xed\x8a\xb8'
    print(bytearray.decode())
    
class Dto:
    def setNum(self, num):
        self.num = num
    def setName(self, name):
        self.name = name
    def getNum(self):
        return self.num
    def getName(self):
        return self.name
    def toString(self):
        return "{번호:" + str(self.num) + ",이름:" + self.name + "}"
    
data1 = Dto()
data1.setNum(1)
data1.setName("park")
data2 = Dto()
data2.setNum(2)
data2.setName("kim")
li = [data1, data2]

import pickle
try:
    with open('./test.txt', 'wb') as f:
        pickle.dump(li, f)
        f.close()
    with open('./test.txt', 'rb') as f:
        result = pickle.loads(f)
        for temp in result:
            print(temp.toString())
        f.close()
except Exception as e:
        print("예외 발생:", e)
finally:
    f.close()

traffic=0

with open('log.txt', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        if log[-1] not in ['-',"'-'",'"-"']:
            traffic+=int(log[-1])
print(traffic)