'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''

import math

rsltlst = []
C=50
H=30
inplst= input("Enter values comman seperated like 1,2,3:-")
print ("List is:- ", inplst)
print(type(inplst))
no_lst = inplst.split(",")
#print(no_lst)


for D in no_lst:
    if(D.isnumeric()):
        n1 = 2*(int(C)*int(D))
        print ("C-{},D-{} & n1-{}".format(C,D,n1) )
        n2 = n1/int(H)
        print ("n2 is:-",n2)
        n3 = math.sqrt(n2)
        print ("value is:-",n3)
        rsltlst.append(str(round(n3)))

    else:
        continue

print (rsltlst)
print (','.join(rsltlst))
