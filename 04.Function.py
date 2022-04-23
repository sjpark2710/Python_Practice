
print("04-01 함수")
print("def는 함수를 만들 때 사용하는 에약어")

print("파이썬 함수의 구조")
def add(a,b):
    return a+b
print("def add(a,b):")
print("  return a+b")

print("입력 값이 없는 함수")
def say():
    return 'Hi'
print("def say():")
print("  return 'Hi'")
print("say()")
print(say())
A = say()
print("결괏값을 받을 변수 = 함수이름()")
print("A = say()")
print(A)

print("결괏값이 없는 함수")
def add(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))

print(add(3,4))

print("입력값도 결괏값도 없는 함수")
def say():
    print('Hi')


print("매개변수를 지정하여 호출하기")
def add(a,b):
    return a+b

result = add(a = 3, b = 4)
print("result = add(a = 3, b = 4)")
print(result)

print("여러 개의 입력값을 받는 함수 만들기")
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,))
print("매개변수 앞에 *가 있으면 튜플로 만들어준다")
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i  in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul("add",1,2,3,4,5)
print(result)

result = add_mul("mul",1,2,3,4,5)
print(result)

print("튜플로 2가지 값을 반환하는 방법")
def add_and_mul(a,b):
    return a+b, a*b

print(add_and_mul(3,4))


print("특별한 상황에 함수를 빠져나가는 방법")
def say_nick(nick):
    if nick =="바보":
        return
    print("나의 별명은 %s입니다."%nick)

say_nick('야호')
say_nick('바보')

print("매개변수 초깃값 미리 설정하기")

