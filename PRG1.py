import math
def cci(a,b,c):
    if (a+b)>c and (b+c)>a and (c+a)>b:
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        cicr = (a*b*c)/(4*area)
        inr = (2*area)/(a+b+c)
        print("area of the circumscribed circle =",cicr)
        print("area of the inscribed circle =",inr)
    else:
        print("Circle cannot be formed by given parameters")
cci(a = int(input("Enter the first side=")),b = int(input("Enter the first side=")),c = int(input("Enter the first side=")))