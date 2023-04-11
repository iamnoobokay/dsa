def multiples(num):
    sum = 0
    listofnums = list()
    for i in range(num):
        curr = i + 0
        if(curr % 3 == 0 or curr % 5 == 0):
            listofnums.append(curr)
            sum = sum+curr
    return sum
        
print(multiples(1000))