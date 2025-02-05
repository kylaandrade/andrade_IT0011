def count_char(st):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    const_count = 0
    space_count = 0
    other_count = 0

    for char in st:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            const_count += 1
        elif char == " ":
            space_count += 1
        else:
            other_count += 1

    return vowel_count, const_count, space_count, other_count

st = input("Enter a string: ")
vowels, consonants, spaces, others = count_char(st)

print("----------------------------------")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Other Characters:", others)