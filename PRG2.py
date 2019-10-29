# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:24:34 2019

@author: sridhar
"""

def nextpri(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                num+=1
                nextpri(num)
                break
            #break
        else:
            print(num,"is prime number")
    else:  
        print(num,",2 is next prime number")
nextpri(int(input("Enter a number: ")))



def nextpri(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                def nextprime1(num):
                    while True:
                        num+=1
                        for i in range(2 , num):
                            if num%i==0:
                                break
                            else:
                                print("next Prime number is=",num)
                                return num
                nextprime1(num)
                break
            #break
        else:
            print(num,"is a prime number")
    else:  
        print(num,"is not a prime number")
nextpri(int(input("Enter a number: ")))
