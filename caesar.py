# 이름 :
# 날짜 :
# 주제 : 시저 암호

# 대문자 65~90
# 소문자 97-122

def caesar(code, codeNum) :
    codeList = list(code)
    actualNum = codeNum % 25
    returnStr = ""
    for i in codeList :
        nTemp = 0
        nSub = 0
        if (i != " ") :
            nTemp = ord(i) + actualNum
            if (ord(i) <= 90 and nTemp > 90) :
                nSub = nTemp - 90
                nTemp = 64 + nSub
            elif (ord(i) <= 122 and nTemp > 122) :
                nSub = nTemp - 122
                nTemp = 96 + nSub

        returnStr += chr(nTemp)
    return returnStr

print("a b c in caesar = ", caesar("A K Y", 4))
# print(2 % 25)
