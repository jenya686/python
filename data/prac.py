name=input("enter your name")
salary = int(input("enter your monthly salary :"))
print(salary)
existing_emi  = int(input("enter you existing monthly emi ;"))
available_emi = salary - existing_emi
min_salary = 50000
min_available_balance = 10000
if salary < min_salary:
    print("your salary is less than minimum salary required for loan")
    