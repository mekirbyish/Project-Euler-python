#a=6
#should return 13

a=10001
prime_numbers=[]
compound_numbers=[]
is_prime=True
i=2
b=0

while b < a:
    is_prime=True
    for x in prime_numbers:
        #check if compound
        if i%x==0:
            compound_numbers.append(i)
            is_prime=False
            break
    #add prime to list
    if is_prime==True:
        prime_numbers.append(i)
        b+=1
    i+=1

prime_numbers.sort()
prime_numbers.reverse()
print(prime_numbers[0])