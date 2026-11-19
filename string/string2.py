name = input("enter your full name")
#remove space
clean_name = name.strip()
#lower case name
normalize_name = clean_name.lower()
print(len(normalize_name))

if normalize_name :
    print(normalize_name[0])
    print(normalize_name[-1])

else:
     print("name cannot be empty")
