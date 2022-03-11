class fraction:
    def __init__(self,numer,denom):
        """
        :param numer:분자
        :param denom:분모
        :return:
        """
        self.a=numer
        self.b=denom
    def __str__(a,b):
        return str(a)+"/"+str(b)
    def __add__(self, other):
        numer1 = self.a*other.b+self.b*other.a
        denom1 = self.b*other.b
        for i in range(1,denom1):
            if numer1%i==0 and denom1%i==0:
                numer1=numer1/i
                denom1=denom1/i
        return fraction.__str__(int(numer1),int(denom1))
    def __sub__(self, other):
        numer2=self.a*other.b-self.b*other.a
        denom2=self.b*other.b
        for i in range(1,denom2):
            if numer2%i==0 and denom2%i==0:
                numer2=numer2/i
                denom2=denom2/i
        return fraction.__str__(int(numer2),int(denom2))
    def __eq__(self, other):
        if self.a/self.b == other.a/other.b:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.a/self.b < other.a/other.b:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.a/self.b > other.a/other.b:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.a/self.b != other.a/other.b:
            return True
        else:
            return False
c1 = fraction(2,4)
c2 = fraction(4,7)
print(c1+c2)
print(c1-c2)
print(c1==c2)
print(c1<c2)
print(c1>c2)
print(c1!=c2)