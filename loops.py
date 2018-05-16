# Looping!

people=['John','Mike','Ben']

for person in people:
    print('Current Person: ', person)

print("--")
# Iterate by Sequence Index
for i in range(len(people)):
    print('Current Person: ', people[i])

print("--")
for i in range(0,3):
    print('Person', i, ': ', people[i])

print("--")

#While loops
"""
while True:
    n = raw_input("Please enter 'hello':")
    if n.strip() == 'hello':
        break
"""
count = 0
while (count < 9):
   print('The count is:', count)
   if count == 5:
       break
   count = count + 1


print("Good bye!")
