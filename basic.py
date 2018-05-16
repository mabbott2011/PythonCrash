#Comments

#This is a single line Comments

"""

This is a multi-line comment

"""
print("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer gravida urna non lorem lacinia, sit amet porta nulla efficitur. Donec justo erat, gravida at auctor quis, interdum ac eros. Suspendisse et dolor non urna sodales porttitor. Maecenas nec commodo eros. Sed pretium condimentum erat non mattis. Donec laoreet malesuada tellus, a congue erat tincidunt id. Vivamus consectetur porttitor mi. Praesent porta scelerisque purus, sed posuere mauris iaculis vel.")

#Let's print a range from the string
print('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'[0:10])

#Numbers don't need quotes
print(1000)


#Printing multiple items on same line
print(1,2,3,'Heya!')

#Printing multiple items on seperate lines
print(1,2,3,'Heya!\nYa made it')

#Only prints one back-slash because it's being escaped
print('C:\\somewhere')

#Adding r (for regular) in front doesn't escape any characters
print(r'C:\\somewhere')
