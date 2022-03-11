"""
A. 프로그래밍이 아닌 수작업으로, C:\temp 디렉토리에 자신의 학번에 해당하는 디렉토리를 생성한 후,
   임의의 파일을 3개 복사한다. 학번 디렉토리 아래에 room1 디렉토리를 만들어서 임의의 파일을 3개 복사한다.
   room1밑에 room2 디렉토리를 만들어서 임의의 파일을 3개 복사한다. 자신의 학번 아래 room3 디렉토리를 만든다.
i. 여러 번 테스트하기 위해, 매번 생성하는 번거로움을 피하게 다른 디렉토리에 복사본을 만들어 놓는다.
B. 아래를 프로그래밍한다.
i. c:\temp아래의 자신의 학번 디렉토리 아래에 있는 모든 파일과 디렉토리를 삭제하라.
   디렉토리인지 확인한 후, 디렉토리라면 해당 디렉토리 내에 있는 모든 파일을 삭제한 후,
   해당 디렉토리를 삭제하라.
ii. 프로그램 실행 후 학번 아래에 파일과 디렉토리가 없음을 확인하라.
    어떤 디렉토리 구조에서도 작동할 수 있게 프로그래밍하라.
iii. 제일 말단 directory 아래 file부터 삭제
"""
import os
i="C:\\Temp\\201732028"
os.chdir(i)
while (1):
    k = os.getcwd()
    t = os.listdir(k)
    if len(t) != 0:
        for b in t:
            u = os.path.join(k, b)
            if os.path.isdir(u):
                if len(os.listdir(u))==0:
                    print(u+"가 비었다.")
                    os.removedirs(u)
                    print(u+" 삭제 완료")
                    os.chdir(i)
                    break
                else:
                    os.chdir(os.path.join(k, b))
                    print(os.getcwd()+"로 이동하였다.")
                    continue
            if os.path.isfile(u):
                os.remove(u)
                print(u+"가 삭제되었다.")
                os.chdir(i)
                continue
    if len(os.listdir(i))==0:
        break
print("끝났당~")