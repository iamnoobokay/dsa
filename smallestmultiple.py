def smallestmultiple():
    
    quotient = 20
    while(True):
        count = 0
        for j in range(21):
            if(j == 0):
                continue
            if quotient % j == 0:
                count = count + 1

            # print(flag)
            if(j == 20 and count == 20):
                return quotient
        quotient = quotient + 1
        # print(quotient)
        
print(smallestmultiple())