prime_numbers_start=[2,3,5,7]
compound_numbers=[4,6,8,9,10]
prime_list=[]
full_prime_list=[]

for number in compound_numbers:
    while number not in prime_numbers_start and number!=1:
        for x in prime_numbers_start:
            print("current number is",number)
            if number%x==0:
                print("divisor is",x)
                print("adding in",x)
                prime_list.append(x)
                number/=x
        if number in prime_numbers_start:
            prime_list.append(int(number))
    print("current prime list is",prime_list)
    #prime_list.sort()
    full_prime_list.append(prime_list.copy())
    prime_list.clear()
print("full prime list is",full_prime_list)