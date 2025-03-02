students = []

def load_records():
    global students
    try:
        with open('students.txt', 'r') as file:
            students = [tuple(line.strip().split(',')) for line in file]
        print(f"Loaded {len(students)} records.")
    except FileNotFoundError:
        print("File not found. Starting with an empty record.")

def save_records():
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(','.join(student) + '\n')
    print("Records saved.")

def show_all_records():
    if not students:
        print("No records found.")
    else:
        for student in students:
            print(student)

def order_by_last_name():
    if not students:
        print("No records to display.")
        return
    for student in sorted(students, key=lambda x: x[1].split()[1]):
        print(student)

def order_by_grade():
    if not students:
        print("No records to display.")
        return
    for student in sorted(students, key=lambda x: (float(x[2]) * 0.6 + float(x[3]) * 0.4), reverse=True):
        print(student)

def add_record(student_id, full_name, class_standing, major_exam_grade):
    students.append((student_id, full_name, class_standing, major_exam_grade))
    print("Record added.")

def main():
    while True:
        print('--------------------------')
        print("Menu:")
        print("1 | Load Records")
        print("2 | Save Records")
        print("3 | Show All Records")
        print("4 | Order by Last Name")
        print("5 | Order by Grade")
        print("6 | Add Record")
        print("0 | Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            load_records()
        elif choice == '2':
            save_records()
        elif choice == '3':
            show_all_records()
        elif choice == '4':
            order_by_last_name()
        elif choice == '5':
            order_by_grade()
        elif choice == '6':
            student_id = input("Enter student ID: ")
            full_name = input("Enter full name: ")
            class_standing = input("Enter class standing: ")
            major_exam_grade = input("Enter major exam grade: ")
            add_record(student_id, full_name, class_standing, major_exam_grade)
        elif choice == '0':
            save_records()
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()