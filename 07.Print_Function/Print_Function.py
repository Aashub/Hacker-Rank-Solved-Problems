if __name__ == '__main__':
    n = int(input())
    
concatinate= ""

# in this for loop is what happening is we have hard codedly set that loop should run from 1 
for i in range(1,n + 1):
    
    # here it will change the integer value into string and and concatinate each i value
    concatinate +=  str(i)
    
print(concatinate)


