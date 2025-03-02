def studentinfo():
    firstn = input("Enter your first name: ")
    lastn = input("Enter your last name: ")
    age = input("Enter your age: ")
    course = input("Enter your course: ")

    student = f"Name: {firstn} {lastn}\nAge: {age}\nCourse: {course}\n"

    with open("students.txt", "a") as file:
        file.write(student)

    print("Student information has been saved to 'students.txt'.")

studentinfo()