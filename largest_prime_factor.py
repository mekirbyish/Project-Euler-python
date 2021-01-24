#a=13195
#prime factors are 5, 7, 13 and 29
a=600851475143
prime_numbers=[]
is_prime=True
i=2
prime_factors=[]

#create prime numbers
while i <= a/2:
    #print("i is",i)
    is_prime=True
    for x in prime_numbers:
        if i%x==0:
            is_prime=False
            #print(i, "is not prime")
            break
    if is_prime==True:
        prime_numbers.append(i)
        #print(i, "is prime")
    i+=1

#find prime factors of number
for x in prime_numbers:
    if a%x==0:
        prime_factors.append(x)

#find largest prime factor
prime_factors.sort()
prime_factors.reverse()
print(prime_factors[0])