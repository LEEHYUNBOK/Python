import os

def remove(b):
    os.chdir(b) # 경로를 옮겨줌
    print(b+"으로 경로를 옮깁니다.")

    if (len(os.listdir(b)) != 0): 				# 만약 b내부에 파일과 폴더가 한 개라도 존재할 시
        print("디렉토리 내부의 파일들을 모두 찾습니다.")
        for name in os.listdir(b):	 			# listdir을 사용, 파일들을 검색
            listFile = os.path.join(b, name) 			# 검색한 파일을 경로와 합쳐 삭제가 유용하게 해줌
            if (os.path.isdir(listFile)): 			# 만약 발견한 것이 폴더일시
                print("\'"+name+"\'"+ "디렉토리를 발견하였습니다.")
                if (len(os.listdir(listFile)) == 0): 		# 그리고 발견한 폴더의 내부가 비어있을 시
                    print("\'" + name + "\'" + "디렉토리의 내부가 비어있어 삭제합니다.")
                    os.removedirs(listFile) 			# 폴더 삭제
                    return remove(b) 				# 재귀로 다시 불러줌
                else: 						# 폴더의 내부에 파일이 존재할 시
                    print("\'" + name + "\'" + "디렉토리의 내부에 파일이 있어 들어갑니다.")
                    return remove(listFile) 			# 재귀로 그 폴더안에 들어가줌

            else: 						# 만약 발견한 것이 파일일 시
                print("\'"+name+"\'"+"파일을 삭제합니다.")
                os.remove(listFile) 				# for문을 이용해 파일들 일괄 삭제

        return remove(b) 					# 그 후 재귀함수로 다시 불러줌

    else: 							# 만약 b내부에 파일과 폴더가 존재하지 않을 시
        print("디렉토리 내부에 파일이 존재하지 않습니다.")
        a = b.count("\\") 					# \의 갯수를 세어주고
        l = b.split("\\", a) 					# \를 기준으로 \의 갯수만큼 b를 나누어줍니다.
        del (l[a]) 						# 그 후, 가장 뒷부분의 요소를 제거하면 상위 폴더로 넘어갑니다.
        b = "" 							# b는 아무것도 없는 상태로 초기화 해줍니다.
        if(len(l) == 1): 					# 만약 'c:'밖에 남지 않은 상태라면 삭제 완료를 알려주고 프로그램을 종료합니다.
            return print("모두 삭제 완료.")
        else: 							# 그게 아니라면 상위 폴더로 이동해 줍니다.
            print("현 디렉토리의 상위 디렉토리로 위치를 옮깁니다.")
            for s in l:
                if (s == "c:"): 				# 'c:'의 앞부분에는 \가 붙지 않으므로 이렇게 처리해 줍니다.
                    b += s
                else: 						# c:가 아닐시 \를 붙여줍니다.
                    b += "\\" + s

            return remove(b) 					# 다쉬 재귀로 함수를 불러줍니다.


s1 = "c:\\temp\\201732028"
								# 디렉토리가 존재하지 않을 수 있으므로 예외처리를 해줌
try:
   remove(s1)

except FileNotFoundError: 					# 예외 FileNotFoundError가 발생하면 적절한 안내문과 함께 에러 안내.
    print("입력한 디렉토리가 존재하지 않습니다.")