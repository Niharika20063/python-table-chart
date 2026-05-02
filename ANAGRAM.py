a = input("Enter any string: ")
b = input("Enter string 2: ")

a1 = "".join(i for i in a if i.isalnum())
b1 = "".join(i for i in b if i.isalnum())

a2 = sorted(a1.lower())
b2 = sorted(b1.lower())

if a2 == b2:
    print("ANAGRAM")
else:
    print("NO")
