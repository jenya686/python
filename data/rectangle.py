length1 = float(input("enter the length of rectangle 1 : "))
breadth1 = float(input("enter the breadth of rectangle 1 : "))
area1 = length1 * breadth1

length2 = float(input("enter the length of rectangle 2 : "))
breadth2 = float(input("enter the breadth of rectangle 2 : "))
area2 = length2 * breadth2

print("/nArea of rectangle 1 : ", area1)
print("/nArea of rectangle 2 : ", area2)
if area1 >area2:
    print("/rectangle 1 is greater than rectangle 2")
else :
    print("rectangle 2 is greater than rectangle 1")