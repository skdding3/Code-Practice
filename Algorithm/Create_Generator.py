def number_generator(stop):
    n = 0              # 숫자는 0부터 시작
    while n < stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n        # 현재 숫자를 바깥으로 전달
        n += 1         # 현재 숫자를 증가시킴
 
for i in number_generator(3):
    print(i)
    
    
    ## retrun 0 1 2
    
    
    # 제너레이터 안에서 변수 n을 만들고 0을 저장합니다. 그리고 while n < stop:과 같이 반복을 끝낼 숫자보다 작을 때 반복하도록 만듭니다. 
    # 반복문 안에서는 yield n으로 숫자를 바깥으로 전달한 뒤 n을 1 증가시키면 됩니다. 
    # 여기서는 yield가 3번 나오므로 for 반복문도 3번 반복합니다.
