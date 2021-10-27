#a=13195
#given number 13195
#prime factors are 5, 7, 13 and 29

a=600851475143

prime_factors=[]
#https://www.pythonpool.com/prime-factorization-python/
import math
def primefactors(n):
    #n odd
    while n%2 == 0:
        #print(2)
        prime_factors.append(2)
        n /= 2
    #n even
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i == 0):
            #print(i)
            prime_factors.append(i)
            n /= i
    if n>2:
        #print(n)
        prime_factors.append(n)
n=int(input("Enter n:"))
primefactors(n)
prime_factors.sort()
prime_factors.reverse()
print("Largest factor: " + str(prime_factors[0]))