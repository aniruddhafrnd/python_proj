'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''
mylst = []
myno = range(2000,3200)

for x in myno:
    if x%7 == 0 and x%5 != 0:
       # print (x)
        mylst.append(str(x))


print (','.join(mylst))
