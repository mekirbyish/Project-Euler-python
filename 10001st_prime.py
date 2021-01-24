#a=6
a=10001
prime_numbers=[]
compound_numbers=[]
is_prime=True
i=2
b=0
while b < a:
    #print("i is",i)
    is_prime=True
    for x in prime_numbers:
        if i%x==0:
            compound_numbers.append(i)
            is_prime=False
            #print(i, "is not prime")
            break
    if is_prime==True:
        prime_numbers.append(i)
        b+=1
        #print(i, "is prime")
    i+=1
prime_numbers.sort()
prime_numbers.reverse()
print(prime_numbers[0])