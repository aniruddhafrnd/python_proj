'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
import sys,os

def cal_fact(num):
    print ("in fuction")
    if num == 1:
        return num
    fact = num * cal_fact(num-1)
    return fact




while True:
    try:
        in_no = int(input("Please provide integer no for factorail:-\n"))
        type(in_no)
        if type(in_no) == int:
            print ("Your number is :-",in_no)
            break
    except ValueError:
        print( " number is not whole number")

fact_no = cal_fact(int(in_no))

print ("Factorial is :-",fact_no)