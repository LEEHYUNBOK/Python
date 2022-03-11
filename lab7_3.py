import os
d = os.getcwd()
k = input("이동 입력할 디렉토리 : ")
os.chdir(d+"\\"+k)
m = input("생성 이동할 디렉토리 : ")
os.mkdir(d+"\\"+k+"\\"+m)
os.makedirs(d+"\\"+k+"\\"+m+"\\test")
print(os.getcwd())
for i in os.listdir():
    print(i)
os.removedirs(d+"\\"+k+"\\"+m+"\\test")
for i in os.listdir():
    print(i)