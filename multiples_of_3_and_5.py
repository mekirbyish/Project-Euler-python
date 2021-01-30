#test number, multiples of 3, 5, 6, 9 and sum of 23
#a=10

a=1000
mult_3_5=[]
i = 1
sum=0

#find multiples of 3 and 5 below limit
while i < a:
    if i%3==0 or i%5==0:
        mult_3_5.append(i)
    i += 1

#sum multiples
for x in mult_3_5:
    sum+=x
print(sum)