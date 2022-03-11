"""
작성일 : 2017.11.15
"""
import re
s = re.compile("a") # apple이 a로 시작하는지 확인
print(s.search("apple"))

print(re.search("[b]","apple")) # apple이 b로 시작하는지 확인

