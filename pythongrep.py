#!/usr/bin/python
import re, sys, os
from stat import *

def walktree(top, regex):
	try:
        for f in os.listdir(top):
            try:
                pathname = os.path.join(top, f)
                mode = os.stat(pathname).st_mode
                if S_ISDIR(mode):
                    walktree(pathname, regex)
                elif S_ISREG(mode):
                    find_in_file(pathname,regex)
                else:
                    print 'Skipping %s' % pathname
            except Exception, e:
                print 'Skipping %s because of %s' % (pathname,e)
 	except Exception, e:
    	print 'Skipping %s because of %s' % (pathname,e)
                
def find_in_file(filename,regex):
	try:
    	handler = open(filename)
       	for line in handler:
    		if re.search(regex, line):
           		print filename + ":" + line,
  	except IOError, e:
    	print "cannot open file - %s" % filename
 	except Exception, e:
    	print 'Skipping %s because of %s' % (filename,e)

regex=sys.argv[1]
inputargs=sys.argv[2::]

for i in inputargs:
   	try:
      	mode=os.stat(i).st_mode
        	if S_ISDIR(mode):
            	walktree(i,regex)
           	elif S_ISREG(mode):
              	find_in_file(i,regex)
          	else:
           		print 'Skipping %s' % i
  	except Exception, e:
     	print 'Skipping %s because of %s' % (i,e)
