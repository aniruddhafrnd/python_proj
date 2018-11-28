'''
Write a program to compute the frequency of the words from the input. The output should output after sorting the key
alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

'''

from operator import itemgetter

freq = {}

print(type(freq))

line = input ("provide input:-")

for word in line.split():
    print (word, freq.get(word,0))
    print ("+ 1", word, freq.get(word,0) + 1)
    freq[word] = freq.get(word,0)+1
    print (freq[word] )

print (freq)

words = freq.keys()
sorted(words)

for w in words:
    print ("%s:%d" % (w,freq[w]))