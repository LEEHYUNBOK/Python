"""
주제 : Recursion을 이용하여 다시 정의한다
작성자 : 이현복
작성일 2017.10.30
"""
def fibo(a):
    if a<2:
        return a
    else:
        return fibo(a-1)+fibo(a-2)
for i in range(0,10):
    print(fibo(i))
