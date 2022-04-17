
print("IF문")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어서 가라")

print("x or y -> x와 y둘 중에 하나만 참이어도 참이다")
print("x and y -> x와 y 모두 참이어야 참이다")
print("not x -> x가 거짓이면 참이다.")

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어서 가라")

print("x in 리스트")
print("x in 튜플")
print("x in 문자열")

1 in [1,2,3]
print(1 in [1,2,3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("\n\n택시를 타고가라")
else:
    print("\n\n걸어서가라")

pocket = ['paper', 'cellphone']
card = True
if 'money'in pocket:
    print("택시를 타고 가라")
elif card:
    print("card가 있으니 택시를 타고 가라")
else:
    print("걸어서 가라")

print('message = "success" if score >= 60 else " failure"')












