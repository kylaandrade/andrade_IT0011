def patta(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "".join(str(x) for x in range(1, i + 1)))

def pattb(n):
    count = 1
    while count <= n:
        if count % 2 == 1:
             print(str(count) * (2 * count - 1))
        count += 1

print("------------------------------------------------------------")
n_a = int(input("Enter the number of rows for the first pattern: "))
patta(n_a)
print("------------------------------------------------------------")
n_b = int(input("Enter the number of rows for the second pattern:"))
pattb(n_b)
print("------------------------------------------------------------")