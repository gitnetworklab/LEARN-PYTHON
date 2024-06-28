# # SECTION-1
# print("PROGRAM TO CHECK IF NUMBER IS 'ODD' OR 'EVEN' !!!")

# num = int(input('Please enter a number :'))

# if num % 2 == 0:
#     print('YES ... Number is EVEN')
# else:
#     print('NO ... Number is ODD')



# # SECTION-2
# print("PROGRAM TO CHECK IF VALUE IS AVAILABLE IN THE LIST !!!")

# users = ['Raju','Satish','Ramesh']
# userInput = str(input('TYPE USER NAME :'))

# if userInput in users:
#     print('Yes, User exist in the list')
# else:
#     print('No, User does not exist in the list')



# SECTION-3
print("PROGRAM TO CHECK WHAT GRADE EMPLOYEE BELONGS TO !!!")

# gradeA = ('Ravi','Nilesh')
# gradeB = ('Seema','Monika')
# gradeC = ('Anant','Satish')

gradeA = ('Analyst','Senior Analyst')
gradeB = ('Associate Consultant','Consultant')
gradeC = ('Senior Consultant','Manager')

myTeam = {
    'Satish':'Manager',
    'Monika':'Consultant',
    'Anant':'Senior Consultant',
    'Ravi':'Analyst',
    'Nilesh':'Senior Analyst'
    }

getUserName = str(input('Please provide User name : '))

if getUserName in myTeam.items() and myTeam.items() in gradeA:
    print('EMPLOYEE BELONG TO GRADE-A.')
elif getUserName in myTeam.items() and myTeam.items() in gradeB:
    print('EMPLOYEE BELONG TO GRADE-B.')
elif getUserName in myTeam.items() and myTeam.items() in gradeC:
    print('EMPLOYEE BELONG TO GRADE-C.')
else:
    print('User Not Found !!!')

