"""
1. 입력한 단어가 a로 시작하는지 확인
2. 입력한 단어가 e로 끝나는지 검사
"""
import re
r = re.compile("^a")
print(r.search("This is a test"))
r = re.compile("e$")
print(r.search("This is a test"))