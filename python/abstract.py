import abc

class Restaurant(metaclass=abc.ABCMeta):
    # 추상 메서드 작성
    @abc.abstractmethod
    def food(self):
        pass

class RestSub(Restaurant):
    def food(self):
        print('im implement')

sub=RestSub()
sub.food()