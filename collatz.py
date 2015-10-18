#!/usr/bin/python
def collatz(begin,listsize=1):
        if begin == 1:
                return listsize
        elif begin % 2 == 0:
                return collatz(begin/2,listsize+1)
        else:
                return collatz(3*begin + 1, listsize+1)

longestlength=0
longestproducer=0
for i in range(1,1000000):
        listsize=collatz(i,1)
        if listsize > longestlength:
                longestlength=listsize
                longestproducer=i

print longestproducer
