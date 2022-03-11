S = input("입력")
t = []
for i in range(0,len(S)):
    print(S[i])
    for a in range(i,len(S)+1):
        t.append(S[i:a])
print(t)
s = set(t)
print(s)
print(len(s))