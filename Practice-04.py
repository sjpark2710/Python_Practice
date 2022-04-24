
print("Q1 : 주어진 자연수가 홀수인지, 짝수인지 판별해 주는 함수 (IS_ODD)를 작성해보자")
def is_odd(number):
    if number %2 ==1:
        return print("홀수입니다.")

    else:
        return print("짝수입니다.")

print(is_odd(7))
print(is_odd(10))

print("\nQ2 : 입력으로 돌아오는 모든 수의 평균 값을 계산해주는 함수를 작성해보자,(단, 입력으로 돌아오는 수의 개수는 정해져 있지 않다")
def average_numbers(*args):
    result = 0
    for i in args:
        result += i
    return print("평균은 %d 입니다"%(result/len(args)))

average_numbers(1,2,3,4,5)
average_numbers(1,2,3)
print("\nQ3 : 다음은 두 개의 숫자를 입력 받아 더하여 돌려주는 프로그램이다.")
input1 = input("1숫자를 입력하세요")
input2 = input("2숫자를 입력하세요")
total  = int(input1) + int(input2)
print("합은 %d입니다"%total)
print("\nQ4 : 다음 중 출력 결과가 다른 것 한 개를 골라 보자")
print("you" "need" "python")
print("you" + "need" + "python")
print("you","need","python")
print("".join(["you","need","python"]))
print("\nQ5 : 다음은 'TEST.TXT'라는 파일에 'Life is too short'문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다")
f1 = open("C:\\Users\\seongjin\\PycharmProjects\\Python-Practice\\test.txt",'w')
f1.write("Life it soo short")
f1.close()
f2 = open("C:\\Users\\seongjin\\PycharmProjects\\Python-Practice\\test.txt",'r')
line = f2.readline()
f2.close()
print(line)
print("\nQ6 : 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다)")
user_input = input("저장할 내용을 입력하세요")
f = open('test.txt','a')
f.write(user_input)
f.write('\n')
f.close()
print("\nQ7 : 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꿔보자")
f= open('C:\\Users\\seongjin\\PycharmProjects\\Python-Practice\\test.txt','r')
body = f.read()
f.close()

body =  body.replace('java','python')

f = open('C:\\Users\\seongjin\\PycharmProjects\\Python-Practice\\test.txt', 'w')
f.write(body)
f.close()

