class Counter:
    def __init__(self, stop):
        self.stop = stop
 
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
 
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
 
for i in Counter(3):
    print(i, end=' ')
    
    
    # Counter(3)[0]을 출력했을 때 0이 나왔습니다. 마찬가지로 Counter(3)[1]은 1, Counter(3)[2]는 2가 나왔습니다. 그리고 for 반복문에 Counter를 사용했을 때도 1, 2, 3이 나왔습니다.
    
    #소스 코드를 잘 보면 __init__ 메서드와 __getitem__ 메서드만 있는데도 동작이 잘 됩니다. 클래스에서 __getitem__만 구현해도 이터레이터가 되며 __iter__, __next__는 생략해도 됩니다(초깃값이 없다면 __init__도 생략 가능).
