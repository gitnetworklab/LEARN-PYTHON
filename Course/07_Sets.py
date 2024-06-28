# Sets are same to that of Dictionary but are unordered and duplicates are not allowed.

mySets = {'Mon','Tue','Wed','Thu','Sat','Sun'}
print(mySets)
print(type(mySets))

mySets.add('Fri') # Adds value to existing set.
print(mySets) # Prints the output.

# If you need only unique from "lists", then convert it into set and use as below.

myList = ['Mon','Tue','Wed','Mon','Wed','Sun'] # Example list created.
print(myList) # Prints the output.

daySets = set(myList) # Coverts "lists" into "sets" to remove duplicates.
print(daySets) # Prints the output.
