#this is how we define the functions.
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
        
        # if year is being perfectly divided by 100 and 400 then it is a leap year
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        # if year is being only being perfectly divided by 100 then it is not a leap year.
        elif year % 100 == 0:
            leap = False
            
    return leap

year = int(input())

# here the function is being called and returned value is being printed out.
print(is_leap(year))