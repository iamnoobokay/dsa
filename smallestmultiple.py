def smallestmultiple():
    
    quotient = 10
    while(True):
        count = 0
        for j in range(11):
            if(j == 0):
                continue
            if quotient % j == 0:
                count = count + 1

            # print(flag)
            if(j == 10 and count == 10):
                return quotient
        quotient = quotient + 1
        # print(quotient)
        
print(smallestmultiple())