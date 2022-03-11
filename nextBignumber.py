def nextBingnumber(smallnumber):
    print(bin(smallnumber))
    ntwo = 0
    num = 0
    nspring = ""
    nsspring = ""
    k=smallnumber
    ntwo=bin(smallnumber)
    nspring=str(ntwo)
    num=nspring.count("1")
    while (1):
        k+=1
        nttwo=bin(k)
        nsspring=str(nttwo)
        if num==nsspring.count("1"):
            print(k)
            print(bin(k))
            break
nextBingnumber(78)