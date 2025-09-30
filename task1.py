student = {"Alice": 98, "Mitchel": 97, "Alex": 82, "William": 66, "Roger": 78, "Ben": 100}
name = input("Enter the student's name: ")
if name in student:
    print(f"{name}'s marks: {student[name]}")
else:
    print("Student not found.")