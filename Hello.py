#Q1: Using the range function , for loop and if/elif/else statements, create a programme
#  that shows all the numbers between 0 and 100 that are divisible by 5,6,7,9 or all of them
number = range(100)
for num in number :
    if num%5==0 and num%6==0 and num%7==0 and num%9==0:
        print(f"{num} is divisible by 5,6,7,9")
    elif num%5==0:
        print(f"{num} is divisible by 5")
    elif num%6==0:
        print(f"{num} is divisible by 6")
    elif num%7==0:
            print(f"{num} is divisible by 7")
    elif num%9==0:
        print(f"{num} is divisible by 9")
    else:
        print(f"{num} is not divisible by 5 or 6 or 7 or 9")        

        

    