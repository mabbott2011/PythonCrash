import os

message = """Lorem ipsum dolor sit amet\n"""

print(os)

# Opens a file
#fo = open('test.txt', 'w')
#Get some info about it!
#print('Name:', fo.name)
#print('Is closed?', fo.closed)
#print('Opening mode:', fo.mode)

#Let's write to it

#fo.write(message)
#print(message)
#fo.close()

# Doesn't seem to write... but it's actually an issue with the working directory of Atom. Open the file in Atom via File explorer to correct this.
fo = open('test.txt','w')
fo.write(message)
print('wrote to ', fo.name)
fo.close()

with open('test2.txt', 'w') as f:
    f.write(message)
    print('wrote to', f.name)


print('')
fr = open('test.txt','r')
print('Reading', fr.name)
print("->",fr.read())
fr.close()



fr = open('test2.txt','r')
print('Reading', fr.name)
print("->",fr.read())
fr.close()
