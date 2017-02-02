

infile = open('contacto_de_JaimeForero.txt', 'r')

#load the full text by lines
text = infile.readlines()

#each line is a part of the message
name = text[0]
date = text[1]
place = text[2]
message  = text[3]

print name
print date
print place
print message
