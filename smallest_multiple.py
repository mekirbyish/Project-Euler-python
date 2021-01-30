#smalles multiple is 2520
#max_numbers=10

max_numbers=20
integer=2
number_list=[]
prime_numbers=[]
compound_numbers=[]
prime_list=[]
full_prime_list=[]
total=1

while integer <= max_numbers:
    is_prime=True
    for x in prime_numbers:
        if integer%x==0:
            is_prime=False
            compound_numbers.append(integer)
            break
    if is_prime==True:
        prime_numbers.append(integer)
    number_list.append(integer)
    integer+=1

for number in compound_numbers:
    while number not in prime_numbers and number!=1:
        for x in prime_numbers:
            if number%x==0:
                prime_list.append(x)
                number/=x
        if number in prime_numbers:
            prime_list.append(int(number))
    full_prime_list.append(prime_list.copy())
    prime_list.clear()

for x in full_prime_list:
    for y in prime_numbers:
        if y in x:
            x.remove(y)
while [] in full_prime_list:
    full_prime_list.remove([])

#this works, but i like the other way better since it follows the guide
"""for i, x in enumerate(full_prime_list):
    for z in x:
        #want y to be position x+1
        for y in full_prime_list[i+1:]:
            if z in y:
                y.remove(z)"""

for x in range(0, len(full_prime_list)):
    for z in full_prime_list[x]:
        for y in full_prime_list[x+1:]:
            if z in y:
                y.remove(z)

for x in prime_numbers:
    total*=x
for x in full_prime_list:
    for y in x:
        total*=y
print(total)