def largestprimes(num):
    i = 2
    number = num
    while(i):
        if(number == i):
            break
        if(number % i) == 0:
            number = number / i
        else:
            i = i + 1
            
    print(number)
    

largestprimes(600851475143)