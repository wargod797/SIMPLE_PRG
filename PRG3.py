#Perfect Square
import math
x = int(input())
def psq(x):
    if (x%math.sqrt(x))==0:
        print(x,"It's a Perfect Square Value")
    else:
        i=0
        while True:
            i+=1
            x+=1
            if (x%math.sqrt(x))==0:
                print("Next Square Value is=",x)
                print("The number Required to add=",i)
                break
            
psq(x)