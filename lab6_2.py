"""
정규식을 이용하여, 사용자가 입력한 영어
문장에서 a,e,i,o,u가 포함되어 있는지 찾아
서 출력하시오. 만족하는 첫번쨰만 출력한다.
[입력] This is a test
"""
import re
r = re.compile("a.e.i.o.u")
print(r.search("This is a test"))