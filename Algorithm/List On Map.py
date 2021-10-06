리스트 = list(map(함수, 리스트))
a = list(map(int, a))
튜플 = tuple(map(함수, 튜플))
 
변수1, 변수2 = list(map(함수, 리스트))    # 언패킹 사용
a, b = list(map(str, range(2)))
 
변수1, 변수2 = map(함수, 리스트)          # 언패킹 사용
a, b = map(int, input().split())


map은 리스트(튜플)의 요소를 지정된 함수로 처리해주는 함수입니다.
백준 문제 풀이시 가장 먼저 해야되는 선언.
