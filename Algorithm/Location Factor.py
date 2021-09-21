# 가장 높은 점수를 구하는 함수

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)
 
max_score = get_max_score(english, science)
print('높은 점수:', max_score)


# return 높은 점수 : 100 
#        높은 점수 : 91


#get_max_score 함수는 호출할 때마다 인수의 개수가 달라지고 있으므로 가변 인수 함수로 만든다.
#get_max_score(korean, english, mathematics, science)처럼 인수를 위치 인수로 넣고 있으므로 def get_max_score(*args):와 같이 만들어 함수 안에서는 max를 사용해서 args에서 가장 큰 수를 구한 뒤 return으로 반환
