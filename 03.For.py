

print("FOR문\n")

print("1. 전형적인 for 문\n")
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print("2. 다양한 for문의 사용 \n")

a = [(1,2), (3,4), (5,6)]
for(first, last) in a:
    print(first + last)

print("for 문의 응용\n")


print("3. for문의 응용\n")

marks = [90, 25, 67, 45, 80]

print("for문과 함께 자주 사용하는 range 함수")
print("range 함수는 숫자 리스트를 자동으로 만들어 준다")
print("range(시작숫자, 끝숫자)   끝숫자는 포함되지 않는다")
a = range(10)
print(a)

a = range(1,11)
print(a)

print("range함수의 예시 살펴보기")
add = 0
for i in range(1,11):
    add = add +i

print(add)








