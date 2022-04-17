'''
홍길동 씨의 과목별 점수는 다음과 같다. 홍길동씨의 평균 점수를 구해보자
과목  점수
국어  80
영어  75
수학  55
'''

print("Q1 : 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동씨의 평균 점수를 구해보자")
국어 = 80
영어 = 75
수학 = 55
평균 = (국어 + 영어 + 수학) / 3
print("평균 : ",평균)

print("Q2 : 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자")
num = 13
if num %2 ==1:
    print("홀수")
else:
    print("짝수")

print("Q3 : 홍길동씨의 줌니등록번호는 881120 - 1068234이다. 홍길동씨의 주민등록번호를 연월일부분과 그 뒤의 숫자부분으로 나누어 출력해 보자")
print("문자열 슬라이싱을 이용")
pin = "881120-1068234"
yyyymmdd = pin[:6]
print("yyyymmdd : ",yyyymmdd)
num = pin[7:]
print("num : ",num)

print("Q4 : 주민등록번호 뒷자리의 맨 첫번째 숫자는 성병을 나타낸다. 주민등록번호에서 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자")
print(pin)
print("성별을 나타내는 숫자는 : ",pin[7])

print("Q5 : 다음과 같은 문자열 a : b: c : d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d#로 바꿔서 출력해보자")
a = "a:b:c:d"
print(a)
b = a.replace(":","#")

print("b = a.replace(':', '#')\nb : ",b)

print("Q6 : [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어 보자")
a = [1,3,5,4,2]
print(a)
a.sort()
print(a.sort())
print(a.reverse())

print("Q7 : ['Life', 'is', 'too', 'short']리스트를 Life is too short 문자열로 만들어 출력해보자")
a = ['Life', 'is','too','short']
result = " ".join(a)
print(result)

print("Q8 : (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해보자")
a = (1,2,3)
print(a)
b = (4,)
c = a + b
print(b)
print(c)

print("Q9 : 다음과 같은 딕셔너리 a가 있다.")
a = dict()
print(a)

print("Q10 : 딕셔너리 a에서 'B'에 해당돠는 값을 추출해보자")
a = {'A' : 90, 'B' : 80, 'C' : 70}
print(a)
result = a['B']
del a['B']
print(result)
print(a)

print("Q11 : a리스트에서 중복 숫자를 제거해 보자")
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
print(aSet)
b = list(aSet)
print(b)

print("Q12 : 파이썬은 다음처럼 동일한 값에 여러개의 변수를 선언 할 수 있다. 다음과 같이 a,b 변수를 선언한 후")
print("a의 두 번쨰 요솟값을 변경하면 b값은 어떻게 될까? 그리고 이런 결과가 나오는 이유에 대해 설명해 보자")
a = b = [1,2,3]
print(a)
print(b)
print(a[1])