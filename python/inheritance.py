# 다중 상속
class Super:
    def sup(self):
        print('im sup')

class Super2:
    def sup(self):
        print('im sup2')

class Sub(Super,Super2):
    def sup(self):
        # super다음 클래스부터의 메서드를 탐색하므로
        # super(Super2,self).sup() 을 하면 attribute error가 발생한다.
        super(Super,self).sup()
        return "im sub"

sub=Sub()
print(sub.sup())