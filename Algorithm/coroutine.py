def number_coroutine():
    while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        print(x)
 
co = number_coroutine()
next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
 
co.send(1)    # 코루틴에 숫자 1을 보냄
co.send(2)    # 코루틴에 숫자 2을 보냄
co.send(3)    # 코루틴에 숫자 3을 보냄


#retrun 1 2 3




# 코루틴 값 보내기 
# 코루틴은 제너레이터의 특별한 형태입니다. 제너레이터는 yield로 값을 발생시켰지만 코루틴은 yield로 값을 받아올 수 있습니다. 
# 다음과 같이 코루틴에 값을 보내면서 코드를 실행할 때는 send 메서드를 사용합니다. 
# 그리고 send 메서드가 보낸 값을 받아오려면 (yield) 형식으로 yield를 괄호로 묶어준 뒤 변수에 저장합니다.
