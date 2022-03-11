print("lab0_2: 이현복")
print("10개의 정수를 입력하세요:")
sum=0
for i in range(0,10):
    r= int(input(""))
    if(r>0 and r<101):
        sum += r
print(sum)