print('집합 자료형')
s1 = set([1,2,3])
print("set()")
print(s1)

s2 = set("Hello")
print(s2)

print("집합 자료형의 특징")
print("-중복을 허용하지 않는다")
print("-순서가 없다(unordered)")

print("set을 리스트로 변환하는 방법")
s1 = set([1,2,3])
print(s1)
l1 = list(s1)
print("l1 = list(s1)")
print(l1)
print(l1[0])

print("교집합, 합집합, 차집합 구하기")
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print("s1 : " ,s1,"s2 : ", s2)

print("교집합\ns1 & s2\n",s1&s2)



