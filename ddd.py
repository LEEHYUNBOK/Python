while(1):
    n=int(input("정수를 입력하세요"))
    s=str(n)
    if (s=="0"):
        break
    sum=0
    k=list(s)
    print(s[-1::-1])
    for i in range(0,len(s)):
        sum+=int(k[i])
    print(sum)
    if (s=="0"):
        break
print("종료합니다.")