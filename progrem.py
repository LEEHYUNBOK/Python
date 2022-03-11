sum = 0
i=0
while(1):
    r= int(input("넣어:"))
    if(r>0 and r<101):
        sum += r
    i=i+1
    if i==10:
        break
print(sum)