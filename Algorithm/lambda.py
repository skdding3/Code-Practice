**Lambda Map**


# list create
cafe = ["cafe1","cafe2","cafe4 cafe5","cafe3"]

#lambda accept
cafe_lamb = map(lambda item: item + ('americano'), cafe)
# -> map(함수, 대상) = list로부터 elements를 하나씩 꺼내서 함수를 적용함. (type(cafe_lamb) = map)

cafe_lamb_list = list(cafe_lamb)

print (cafe_lamb)
# return : <map object at 0x7fdfd116b670>
print (cafe_lamb_list)
# return : ['cafe1americano', 'cafe2americano', 'cafe4 cafe5americano', 'cafe3americano']






**Lambda Filter**
# list create
starbucks = ['americano','latte','mocha','milktea']

#lambda accept
result = filter(lambda member: len(member) > 6, starbucks)

#list method
result_list = list(result)

print(result_list)

#return : ['americano', 'milktea']

#filter method 활용해서 6자리 초과된 단어 색출
