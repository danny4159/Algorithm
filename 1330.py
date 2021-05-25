#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

a, b = input('숫자 두개입력 : ').split()
a=int(a)
b=int(b)
if a>b:
    print(">")
elif a<b:
    print("<")
elif a==b:
    print("==")
        
    

