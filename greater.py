print("This is the tester which number is greater in four number. ")
number1 = float(input("Enter the first number :- "))
number2 = float(input("Enter the second number :- "))
number3 = float(input("Enter the third number :- "))
number4 = float(input("Enter the fourth number :- "))

if (number1 > number2) and (number1 > number3) and (number1 > number4) :
    print("Number 1" , number1 , "is greater from all numbers")
elif (number2 > number1) and (number2 > number3) and (number2 > number4) :
    print("Number 2" , number2 , "is greater than all numbers . ")
elif (number3 > number1) and (number3 > number2) and (number3 > number4) : 
    print("Number 3 " , number3 , "is greater than all numbers")
elif (number4 > number1) and (number4 > number2) and (number4 > number3) :
    print("Number 4" , number4 , "is greater than all numbers")
elif (number1 == number2 == number3 == number4) : 
    print("All numbers have same value .")
else : 
    print("Number error !")