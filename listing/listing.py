marks = [75 , 85 , 92 , 67 , 74]
print("orignal adding" , marks)
#append
marks.append(88)
print("after adding" , marks)
#insert
marks.insert(1,89)
print("after inserting" , marks)
#remove
marks.remove(67)
print("after removing" , marks)
#sort
marks.sort()
print("after sorting" , marks)
#total
print("total students" , len(marks))
#check existing marks
print(23 in marks)
print(85 in marks)
#search marks
search = int(input("enter marks to search"))
for mark in marks:
 print(mark)