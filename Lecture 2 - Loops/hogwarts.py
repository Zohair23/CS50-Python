#list
students = ["Hermione", "Harry", "Ron"]

#basic print using each individual index
print(students[0])
print(students[1])
print(students[2])

#using a for loop, python automatically assigns each initialises student in students to the student variable
#all students are printed here
for student in students:
    print(student)

#another version
for i in range(len(students)):
    print(students[i])




#dict

# 2 lists
#here we want to try and associate one item from a list to another item from a list
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# to do this we use
# Hermione -> Gryffindor, Harry -> Gryffindor and so on...
# basically we made a dictionary here
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"]) # here a dictionary is used, it searches for Hermione, and prints what is
                            # associated with it, so it would print Gryffindor,


# but if we were to use a for loop over this
for student in students:
    print(student) # by default python will print just the "keys", just the names, Hermione, Harry, etc.

#if you want to print both
for student in students:
    print(student, students[student], sep=", ") # first the student is printed, then python uses the dictionary
                                      # to search for the student, and output back what it associates with
                                      # sep=", " to just add a comma inbetween


# 4 dictionaries example
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, # 1st dictionary
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

#print all of them with a comma seperating them
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")