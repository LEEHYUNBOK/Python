"""
1. tes?t tes"t tes+t를 검사하는 정규식 정의
    A. <입력 예> test, tet, tesst 결과가 어떻게
       다르게 나오는지 확인
"""
import re
r = re.compile("tes?t")
print(r.search("This is a test"))
c = re.compile("tes*t")
print(c.search("This is a test"))
d = re.compile("tes+t")
print(d.search("This is a test"))