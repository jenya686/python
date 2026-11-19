numbers = [10,20,30,40,50]
print("orignal numbers", numbers)

index = numbers.index(30)
print("index of 30 is ",index)

numbers[index] = 35 
print("after replacement" , numbers)

new_numbers = numbers.copy()
print("copied list", new_numbers)

