
print("While 문")

treeHit = 0
while treeHit <10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다."%treeHit)
    if treeHit ==10:
        print("나무 넘어갑니다.")

print("4를 입력하면 빠져나가는 while 문")
prompt = """
1. add
2. del
3. list
4. quit
enter number : """


number = 0
while number != 4:
    print(prompt)
    number = int(input())



print("\n커피 while문\n")
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다."%coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다.")
        break












