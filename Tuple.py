
print("리스트는 []으로 둘러싸지만, 튜플은 ()으로 둘러싼다")
print("리스트는 그 값의 생성, 삭제, 수정이 가능하지만, 튜플은 그 값을 바꿀 수 없다")

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b',('ab', 'cd'))

print("1.튜플 요솟값을 삭제하려 할 때")
t1 = (1,2,'a','b')
print(t1)
print("del t1[0], 및 t1[0] = 0으로 수정할려고 하면 오류가 발생")

print("튜플 다루기")
print("1 index 인덱싱하기")
t1 = (1,2,'a','b')
print(t1)
print(t1[0])
print(t1[3])

print("2. 슬라이싱하기")
t1 = (1,2,'a','b')
print(t1)
print(t1[1:])

print("3.튜플 더하기")
t2 = (3,4)
print(t1 + t2)

print("4. 튜플 곱하기")
t2 * 3
print(t2 * 3)

print("5. 튜플 길이 구하기")
t1 = [1,2,'a','b']
print(t1)
print(len(t1))
print("Q.(1,2,3)에서 (1,2,3,4)만들기")
a1 = (1,2,3)
print(a1)
b1 = a1 +(4,)
print(b1)




