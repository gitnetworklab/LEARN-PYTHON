# Dictionary must be defined within Curly Braces {}.
myTeam = {
    'fName':'Satish',
    'lName':'Bodhgire',
    'Designation':'Manager',
    'Experience':17,
    'Working':True
    }

myMarks = {
    'Marathi':80,
    'Hindi':85,
    'English':92,
    'Maths':35,
}
print(myMarks)
print(type(myMarks))

print(myMarks.get('Marathi'))
print(myMarks.get('Hindi'))
print(myMarks.get('English'))
print(myMarks.get('Maths'))
print(myMarks.get('Gujrathi')) # If any undefined Key been called, "get" ensures there won't be any error, but the value "None" returns.

myMarks['Science'] = 87 # Add additional "Key:Value" in the existing dictionary.
print(myMarks) # Prints the output.

del myMarks['English'] # Delete specific "Key:Value" in the existing dictionary.
print(myMarks) # Prints the output.

print(len(myMarks)) # Shows total number of "Key:Value" pairs in the dictionary.