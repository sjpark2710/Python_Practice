print("딕셔너리")
print("딕셔너리의 모습 : {Key1 : Vaule1, Key2 : Value2, Key3 : Value3...}")

print("딕셔너리를 어떻게 만들까?")
dic = {'name' : 'pey', 'phone ' : '0119993323', 'birth' : '1118'}
print(dic)

a = {1 : 'hi'}
print(a)

a = {'a' : [1,2,3]}
print(a)

print("1. 딕셔너리 쌍 추가, 삭제하기")
a = {1 : 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

print("2. 딕셔너리 요소 삭제하기")
print(a)
del a[1]
print(a)

print("딕셔너리를 사용하는 방법")
print("1. 딕셔너리에서 key 사용해 value 얻기")
grade = {'pey' : 10, 'julliet' : 90}
print(grade)
print(grade['pey'])
print(grade['julliet'])

a = {1 : 'a', 2 : 'b'}
print(a)
print(a[1])
print(a[2])

a = {'a' : 1, 'b' : 2}
print(a)
print(a['a'])
print(a['b'])

dic = {'name' : 'pey', 'phone' : '0119993233', 'birth' : 1118}
print(dic)
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

print("2. 딕셔너리 만들때 주의할 사항")
a = {1 : 'a', 1 : 'b'}
print("a = {1 : 'a', 1 : 'b'}")
print(a)
print("key 값이 중복되면, 최근의 값이 적용된다.")

print("딕셔너리 관련 함수")

print("Key 리스트 만들기(keys)")

a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
a.keys()
print(a.keys())
print("for 함수 사용 하는 방법")
for k in a.keys():
    print(k)

print("리스트를 활용하는 방법")
list(a.keys())
print(list(a.keys()))

print("value 리스트 만들기(values")
a.values()
print(a.values())

print("key, value 쌍 얻기(items)")
a.items()
print(a.items())

print("key : value 쌍 모두 지우기 ( clear)")
a.clear();
print("a.clear()")
print(a)

print("key로 value 얻기(get)")
a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
a.get('name')
print(a.get('name'))

print(a.get('phone'))

print("해당 key가 딕셔너리 안에 있는지 조사하기(in")
a = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
print('name' in a)
print('email'  in a)



