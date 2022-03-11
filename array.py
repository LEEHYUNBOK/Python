p = int(input("정수 입력 : "))
a=[]
for i in range(1, 100000):
    if i % 2 == 0:
        d = i
        n = 1
        while (1):
            k = str(n) + "/" + str(d)
            a.append(k)
            d-=1
            n+=1
            if d==0:
                break
    elif i % 2 == 1:
        d = 1
        n = i
        while (1):
            k = str(n) + "/" + str(d)
            a.append(k)
            d+=1
            n-=1
            if n==0:
                break
    if len(a)>=p:
        print(a[p-1])
        break