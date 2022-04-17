

print("자료형의 값을 저장하는 공간, 변수")
a = [1,2,3]
print("a주소가 가리키는 메모리의 주소")
print("id(a) : ",id(a))

print("리스트를 복사할 때")
a = [1,2,3,]
b= a
print("a = [1,2,3]일떄,a = b를 하면 둘다 같은 물리적 주소를 같는다.")
print("a = b , id(a) : ", id(a), "id(b) : ", id(b))
print("a is b : ", a is b)
a[1] = 4
print("a[1] = 4 와 같이 변경을 하면 a와 b는 같이 변경된다.\na :",a,"b : ",b)

print("1.[:]사용")
a = [1,2,3]
print(a)
b = a[:]
print("b = a[:] : ", b)
a[1] = 4
print("a[1] = 4\na : ", a,"\nb : ",b)

print("2. copy 모듈 사용")
print("from copy import copy")
a = [1,2,3]
print(a)
print('b = copy(a)\nb : ',b)
print('a is b : ', a is b)

a,b = ('python', 'life')
print("a, b = ('python', 'life')\na : ",a,'b : ',b)

print("\n\n(a,b) ='python', 'life'\na : ",a,"b : ",b )



