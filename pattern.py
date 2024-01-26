value = int(input("Enter how many rows you wnat to make pattern :- "))

for i in range(1 , value + 1):
    for x in range( 1 , i + 1):
        print("*" , end = "")
    print()