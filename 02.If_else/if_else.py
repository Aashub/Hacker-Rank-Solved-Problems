
# here we are taking input integer input and storing it in "n" variable
n = int(input(""))

# if input is not divisible by 2 then it was going to print
if n % 2 != 0:
    print("Weird")
    
# if input is  divisible by 2 then this condition wil run
elif n % 2 == 0:
    if n > 2 and n < 5:
        print("Not Weird")
    
    elif n >= 6 and n <= 20:
        print("Weird")
    
    elif n > 20:
        print("Not Weird")

