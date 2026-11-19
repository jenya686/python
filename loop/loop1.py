# for number in range(2 , 7):
#  print(number)
# for number in range(342 , 769 , 6):
#     print(number)

# a = int(input("enter first number"))
# b = int(input("enter second number"))
# for number in range (a , b+1):
#  if(number % 2 == 0) :
#     print(number)

# number = int(input("enter a number"))
# count = int(input("how many multiples do u need"))
# for i in range (1 , count + 1):
#     multiple = i * number
#     print(multiple)

# a = int(input("enter first number"))
# b = int(input("enter last number"))
# d = int(input("enter the divisor"))
# for i in range (a , b+1):
#  if (i % 4 == 0):
#   print(i)

# a = int(input("enter start : "))
# b = int(input("enter last : "))
# for i in range (a , b+1 , -1):
#  print(i)


a = int(input("enter start : "))
b = int(input("enter last : "))

print("acscending order : ")
for i in range(a , b+1) :
 print(i)

print("even numbers : ")
for i in range(a , b+1) :
    if(i % 2 == 0) :
        print(i)

print("first five multiple")
multi= int(input("enter a number"))
for i in range (1 , 6):
    multiple = i * multi
    print(multiple)

print("reverse sequence")
for i in range (b , a +1, -1) :
    print(i)