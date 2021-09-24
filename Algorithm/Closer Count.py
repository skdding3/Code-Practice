# 호출 횟수를 세는 함수 (클로저 사용용)

def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
                       
 
c = counter()
for i in range(10):
    print(c(), end=' ')


# return : 1 2 3 4 5

#함수 counter를 호출해서 반환값을 c에 저장한 뒤에 c를 호출
# c를 호출할 때마다 값이 계속 유지되게 하려면 함수를 클로저로 만들어야 한다.
