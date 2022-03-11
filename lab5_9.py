"""
주제 : 매개변수로 넘어오는 x번째 피보나치 수를 반환하는 함수 fibo를 정의하라
작성자 : 이현복
작성일 2017.10.30
"""
def fibo(a):
    b=0
    c=1
    print(b)
    d=0
    for i in range(0,a-1):
        b=c
        c=d
        d=c+b
        print(d)
fibo(10)
