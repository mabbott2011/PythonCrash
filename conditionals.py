# Conditionals

x = 4

#basic if
if x < 6:
    print('This is true')


#basic If Else
y = 1
if y > 6:
    print("This is true")
else:
    print("This is false")


# Elif
color = 'red'
#color = 'blue'
#color = 'purple'

if color == 'red':
    print('Color is red')
elif color == 'blue':
    print('Color is blue')
else:
    print('Color is neither red or blue')



#Nested if
if color == 'red':
    if x < 10:
        print('This is true')

#But lets write this better
if color == 'red' and x < 10:
    print('This is a true statement')
