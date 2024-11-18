if __name__ == '__main__':
    n = int(input())
 
sq = 0

# The for loop in Python is used to iterate over a sequence like a list, tuple, or string or other iterable object,
# the loop runs until does reach out its last digit for suppose if we want to run till 3 times then it runs till three times
# and then it will end and exit the for loop.
for i in range(n):
    
    # ** operaands what acutally do is it  raises a number to a specified power. which in this this case is it raises the power by 2
    # example 2**2 = 4, 3**2 = 9
    sq = i ** 2
    print(sq)
    
