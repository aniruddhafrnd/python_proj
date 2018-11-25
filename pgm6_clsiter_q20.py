'''
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

'''

# class gen:
#     def __init__(self, max):
#         self.max = max
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.num += 1
#
#         if self.num < self.max:
#             if check_div(self.num):
#                 return self.num
#
#
#         else:
#             raise StopIteration
#
#
# def check_div(number):
#     if number%7 == 0:
#         return True
#     else:
#         return False
#
#
#
# rslt = []
#
# mygen = gen(40)
#
#
# for x in mygen:
#     if x!= None:
#         print(x)
#


'''
another method to do this is as below, use of yield function
'''

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        #print ("inside ",i)
        if j%7==0:
            yield j
            #print("inside yield", j)

for i in putNumbers(10):
    print (i)



