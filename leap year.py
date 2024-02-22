a=int(input("enter the year"))
if a%400==0:
    print("leap year")
else:
    if a%4==0 and a%100!=0:
        print("leap year")
    else:
        print("non leap year")

     
