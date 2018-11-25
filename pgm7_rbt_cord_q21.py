'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''

import math

sttpl = (0,0)
intpl = []
new_x = 0
new_y = 0
n = 0

while True:
    line = input("Provide input tuples for direction:")

    if line:
        intpl.append(tuple(line.split(" ")))
    else:
        break

# print (intpl)
#
# print ("single element", type(intpl[0]))
# myX,myY = intpl[0]
#
# print (myX,myY)

for n in intpl:

    dir,pos = n

    if dir == 'UP':
        new_x += int(pos);
    elif dir == 'DOWN':
        new_x -= int(pos);
    elif dir == 'LEFT':
        new_y += int(pos);
    elif dir == 'RIGHT':
        new_y -= int(pos);



print (new_x,new_y)


print (int(round(math.sqrt(new_y**2 + new_x**2))))