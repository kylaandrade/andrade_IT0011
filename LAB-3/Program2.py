def string_manip():
    firstn = input("Enter your first name: ")
    lastn = input("Enter your last name: ")

    fulln = firstn + " " + lastn
    uppern = fulln.upper()
    lowern = fulln.lower()
    namelength = len(fulln)

    print("Full Name (Upper Case):", uppern)
    print("Full Name (Lower Case):", lowern)
    print("Length of Name:", namelength)

string_manip()