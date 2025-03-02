def string_manip():
    firstn = input("Enter your first name: ")
    lastn = input("Enter your last name: ")
    age = input("Enter your age: ")

    fulln = firstn + " " + lastn
    slicedn = firstn[:3]
    greetingmsg = "Hello, " + slicedn + "! Welcome. You are " + age + " years old."

    print("--------------------------------------------")
    print("Full Name:", fulln)
    print("Sliced Name:", slicedn)
    print("Greeting Message:", greetingmsg)

string_manip()