## print tuple 
##tuple is for storing values.
## list - stores same type of values.
## tuple - stores different type of values or diff data type.

# profile = ("Jenya" , 9019 , "MATHS" , 80)
# print (profile)

# #negative indexing
# print (profile[-1])
# print (profile[-2])

# #is it tuple or not ?

# #int
# x = (10)
# print(type(x))
# #tuple
# x = (10 ,)
# print (type(x))
# profile = ("Jenya" , 9019 , "MATHS" , 80)

##normal indexing
# name = profile[0]
# roll = profile[1]
# subject = profile[2]
# marks = profile[3]

# print(name)
# print(roll)
# print(branch)
# print(marks)

##unpacking tuple
# student = ("Jenya" , 9019 , "MATHS" , 80)
# teacher = ("gourav" , 2342 , "CST" , 24)
# name , roll no , subject , marks = student
# name , roll no , subject , age = teacher
# print(name)
# print(roll)
# print(branch)
# print(marks)
# print(age)

# #calculate percentage of student marks
# student = ("riya" , 91 , 98 , 95 , 94)
# #unpack the tupple
# name , m1 , m2 , m3 , m4 = student
# #total marks
# total = m1 + m2 + m3 + m4
# #total percentage
# percentage = (total / 400) * 100
# print(name)
# print(total)
# print(percentage)

# #is modification possible in tuple ?
# marks = ( 91 , 98 , 95 , 94)
# marks[1] = 89
# print(marks)

# #but list support
# data = [10 , 23 , 45 , 53 , 28]
# data[1] = 89
# print(data)



