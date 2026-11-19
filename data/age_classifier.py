n = int(input("enter consumption in n"))
if n>0 and n<=100 :
    print("low consumption")
elif n>100 and n<=200 :
    print("moderate consumption")
elif n>200 and n<=500 :
    print("high consumption")