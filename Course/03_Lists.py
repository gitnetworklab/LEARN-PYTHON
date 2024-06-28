# Create a list using brackets as below.
laptopModels = ['HP','Lenovo','Dell','SONY','Acer']

print(laptopModels) # Print the entire list.
print(laptopModels[2]) # Print the index 2 in ordered list.
print(laptopModels[3]) # Print the index 3 in ordered list.

laptopModels.append('Chromebook') # Append any other value in existing list.
print(laptopModels) # Print the entire list.
print(laptopModels[5]) # Print the index 5 (appended) in ordered list.

laptopModels.remove('Dell') # Remove specific value in existing list.
print(laptopModels) # Print the entire list.

laptopModels[2] = 'Sony' # Modify specific value in the list.
print(laptopModels) # Print the entire list.

laptopModels.insert(2,'Asus') # Inserts specific value in existing list at defined index.
print(laptopModels) # Print the entire list.

del laptopModels[2] # Deletes specific index in the list as opposed to value in above.
print(laptopModels) # Print the entire list.

print(len(laptopModels)) # Print the number of values in the list.

laptopModels.sort() # Sort the list in alphabetical order.
print(laptopModels) # Print the entire list.

laptopModels.sort(reverse=True) # Sort the list in reverse-alphabetical order.
print(laptopModels) # Print the entire list.

laptopModels.reverse() # Sort the list in reverse order (Not alphabetical order).
print(laptopModels) # Print the entire list.

#laptopModels.pop() # Pops-out the last value.
#print(laptopModels) # Print the entire list.

#laptopModels.pop(1) # Pops-out the indexed value in the list.
#print(laptopModels) # Print the entire list.

print(laptopModels[:3]) # Print the slices of the values in the list.