# Escape characters.
'''
Multiline comment
Test line 1
Test line 2
'''

print("Welcome to Python.\nCoding a program.")          # "\n" is the escape character for new line.
print("Welcome to \"Python\".\nCoding a program.")      # "\" is the escape character to skip general builtin characters by Python. Here "Double Quotes".
print("Welcome","to","Python", sep="-")                 # Separator can be used to separate the values with certain string. (Default is blank space.)
print("Welcome","to","Python", end="!!!\n")             # Values can be end by specific character. "\n" for new line at the end.

