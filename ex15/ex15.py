from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Here's your filename again:"
file_again = raw_input("> ")

txt_again = open(file_agin)

print txt_again.read()