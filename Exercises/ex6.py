# More complex strings, variables & formatting

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x # Print's the sentence, taking the previously declared variables as format characters
print y

print "I said: %r." % x # Takes the sentence variables as format characters, which take variables as format characters
print "I also said: '%s'." % y

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r" # Declares a variable which requires a format character

print joke_evaluation % hilarious # Prints the variable requiring a format character, with the "hilarious" variable as the format character

w = "This is the left side of..."
e = "a string with a right side"

print w + e

#print joke_evaluation # To see what happens when no format character is supplied