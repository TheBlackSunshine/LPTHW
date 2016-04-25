# Taking arguments direct from the command line when ran

from sys import argv

script, first, second, third = argv # The arguments variable holds args passed to script when ran

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third