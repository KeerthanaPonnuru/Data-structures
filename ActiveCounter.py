import sys
import random
from functools import reduce


l=[2,16]
res = reduce(lambda x, y: x ^ y, l)

ul  =  res - 1
i,cn = 0,0
p  =  1
val=1000000

while(i<val):
    if (random.randint(1,sys.maxsize) % p) != 0:
    	pass
    else:
        cn += 1
        if cn <= ul:
        	pass
        else:
            p *= 2
            cn = cn >> 1
    i=i+1


activeCounter =  cn * p

doc = open("output3.txt", 'w')

print(str(activeCounter),file=doc)
