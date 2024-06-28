# # SECTION-1
# for a in 1,2,51:
#     print(a)

# userList = ['Rahul','Narendra','Rajeev','Mahesh']
# for user in userList:
#     print(user)



# SECTION-2
myMarks = {
    'Marathi':80,
    'Hindi':85,
    'English':92,
    'Maths':35,
    }

for subjects,marks in myMarks.items():
    print(f'Subject is {subjects}')
    print(f'Marks are {marks}')

for subjects in myMarks.keys():
    print(subjects)
for marks in myMarks.values():
    print(marks)