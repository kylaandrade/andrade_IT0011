def studentinfo():
    firstn = input("Enter your first name: ")
    lastn = input("Enter your last name: ")
    age = input("Enter your age: ")
    contactnmbr = input("Enter your contact number: ")
    course = input("Enter your course: ")

    student = f"First Name: {firstn}\nLast Name: {lastn}\nAge: {age}\nContact Number: {contactnmbr}\nCourse: {course}\n"
    with open("students.txt", "a") as file:
        file.write(student)

    print("Student information has been saved to 'students.txt'.")

studentinfo()