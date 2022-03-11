import os
try:
    dict=input("디렉토리 입력하시오 : ")
    os.chdir(dict)
    f=open("score.txt","r")#
except FileNotFoundError:
    print("파일이 없음")
score1=f.readlines()
ksum=0
msum=0
esum=0
name=[]
kl=[]
ml=[]
el=[]
score=[]
for i in score1:
    str1=str(i)
    str2=str1.split(":")
    for t in str2:
        if t =="\n":
           t=t.split("\n")
        score.append(t)
for i in range(0,len(score)):
    if i%4 == 0:
        name.append(score[i])
    if i%4 == 1:
        kl.append(int(score[i]))
    if i%4 == 2:
        ml.append(int(score[i]))
    if i%4 == 3:
        el.append(int(score[i]))
for t in kl:
    ksum+=int(t)
for d in ml:
    msum+=int(d)
for q in el:
    esum+=int(q)
for w in range(0,len(name)):
    rsum = 0
    rsum = int(kl[w])+int(ml[w])+int(el[w])
    print(str(name[w]) + " 평균 : " + str(int(rsum)//3))
print("국어평균 : ", ksum/len(kl))
print("수학평균 : ", msum/len(ml))
print("영어평균 : ", esum/len(el))
