#a=10
a=2000000
prime_numbers=[]
sum=0
i=2
while i < a:
    print("i is",i)
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
for x in prime_numbers:
    sum+=x
print(sum)