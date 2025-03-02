def readstudentinf():
    with open("students.txt", "r") as file:
        contents = file.readlines()

        print("Reading Student Information:")
        for line in contents:
            print(line.strip())

readstudentinf()