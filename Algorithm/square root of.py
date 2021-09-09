def part2(a):
    b = [] # 제곱수 저장
    c = [] # 홀/짝수 저장

    b = list(map(lambda x : x**2, a))
    print(b)

    for i in b:
        if i%2 == 0: # 짝수
            c.append("짝수")
        else:
            c.append("홀수")
    print(c)

    return b, c 

if __name__ == "__main__":
    part2([1, 2, 3, 4, 5])