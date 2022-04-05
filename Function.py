a = "hobby"
a

#문자 개수 세기count 함수
print("문자 개수 세기count 함수")
print(a)
a.count('b')
print(a.count('b'))

'''
위치 알려주기 1 find 함수
'''
print("위치 알려주기 1 find 함수")
c = "Python is the best choice"
a.find('c')
print(c.find('c'))
print(c.find('P'))

#위치 알려주기 2 index 함수
print("위치 알려주기 2 index 함수")
a = "Life is too short"
print(a)
a.index('i')
print(a.index('i'), a.index('t'))

#문자열 삽입 join 함수
print("문자열 삽입 join 함수")
",".join('abcd')

print(",".join('abcd'))

#소문자를 대문자로 바꾸기 upper 함수
print("소문자를 대문자로 바꾸기 upper 함수")
a = "hi"
print(a)
a.upper()
print(a.upper())

#대문자를 소문자로 바꾸기 lower
print("대문자를 소문자로 바꾸기 lower")

a = "HI"
print(a)
a.lower()
print(a.lower())


#왼쪽 공백 지우기 lstrip

print("왼쪽 공백 지우기 lstrip")
a = "   hi"
print(a)
a.lstrip()
print(a.lstrip())

#오른쪽 공백 지우기  rstip
print("오른쪽 공백 지우기  rstip")
a = "hi      "
print(a)
a.rstrip()
print(a.rstrip())

#양쪽 공백 지우기 strip
print("양쪽 공백 지우기 strip")
a = "   hi    "
print(a)
a.strip()
print(a.strip())

#문자열 바꾸기 replace
print("문자열 바꾸기 replace")
a = "Life is too short"
print(a)
a.replace("Life" , "Your leg")
print(a.replace("Life" , "Your leg"))

#문자열 나누기 split
print("문자열 나누기 split")
a = "Life is too short"
print(a)
a.split()
print(a.split())
b = "a:b:c:d"
print(b)
print(b.split(':'))