
#리스트명 = [요소1, 요소2, 요소3....]
odd = [1,3,5,7,9]
print(odd)

a = []
b = [1,2,3]
c = ['Life', 'is','too','short']
d = [1,2,'Life','is']
e = [1,2, ['Life', 'is']]

print(a)
print(b)
print(c)
print(d)
print(e)

#리스트 인덱싱
print("리스트 인덱싱")
a = [1,2,3]
print(a)

print(a[0])
print(a[0] + a[2])
print(a[-1])

a=[1,2,3,['a', 'b', 'c']]
print(a)

print(a[0])
print(a[-1])
print(a[3])

print(a[-1][0])

print(a[-1][2])

a = [1,2, ['1', 'b', ["Life", "is"]]]
print(a)
print(a[2][0])
print(a[2][2])
print(a[2][2][1])

#리스트 슬라이싱
print("리스트 슬라이싱")
a = [1,2,3,4,5]
print(a)
a[0:2]
print(a[0:2])

a = "12345"
print(a)
print(a[0:2])

a = [1,2,3,['a', 'b', 'c'],4,5]
print(a)

print(a[2:5])
print(a[3][:2])

#리스트 더하기
print("리스트 더하기")
a = [1,2,3]
b = [4,5,6]
print(a)
print(b)
print(a+b)

print(a*3)
#리스트 길이 구하기
print("리스트 길이 구하기")
print(len(a))

#리스트에서 값 수정하기
print("리스트에서 값 수정하기")
a = [1,2,3]
print(a)
a[2] = 4
print(a)

#del 함수 사용해 리스트 요소 삭제하기
print("del 함수 사용해 리스트 요소 삭제하기")
a = [1,2,3]
print(a)
del a[1]
print(a)

a = [1,2,3,4,5]
print(a)
del a[2:]
print(a)

#리스트 관련 함수
print("리스트 관련 함수")
a = [1,2,3]
print(a)
#리스트에 요소 추가  append
print("리스트에 요소 추가  append")
a.append(4)
print(a)
a.append([5,6])
print(a)

#리스트 정렬  sort
print("리스트 정렬  sort")

a = [1,4,3,2]
print(a)
a.sort();
print(a.sort())

a = ['a','c','b']
print(a)
a.sort()



#리스트 뒤집기 reverse
print("리스트 뒤집기 reverse")
a = ['a','c', 'b']
print(a)
a.reverse()
print(a)

#리스트 위치 반환(index)
print("리스트 위치 반환(index)")
a = [1,2,3]
print(a)
print(a.index(2))
print(a.index(3))

#리스트 요소에 삽입(insert)
print("리스트 요소에 삽입(insert)")
a = [1,2,3]
print(a)
a.insert(0,4)
print(a)
a.insert(3,5)
print(a)

#리스트 요소 제거(remove)
print("리스트 요소 제거(remove)")
a = [1,2,3,1,2,3]
print(a)
a.remove(3)
print(a)
a.remove(3)
print(a)

#리스트 요소 끄집어 내기(pop)
print("리스트 요소 끄집어 내기(pop)")
a = [1,2,3]
print(a)
a.pop()
print(a)

a = [1,2,3]
print(a)
a.pop(1)
print(a)

#리스트에 포함된 요소x의 개수 세기(count)
print("리스트에 포함된 요소x의 개수 세기(count)")
a = [1,2,3,1]
print(a)
print(a.count(1))

#리스트 확장(extend)
print("리스트 확장(extend)")
a = [1,2,3]
print(a)
a.extend([4,5])
print(a)
b = [6,7]
print(b)
a.extend(b)
print(a)



