def sum(st):
    total = 0
    for char in st:
        if char.isdigit():
            total += int(char)
    print("Sum:", total)

print("-------------------------------------")
input_string = input("Enter string: ")
sum(input_string)
print("-------------------------------------")