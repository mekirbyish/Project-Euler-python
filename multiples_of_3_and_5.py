#example
mult_3_5=[]
i = 1
while i < 10:
    if i%3==0 or i%5==0:
        mult_3_5.append(i)
    i += 1
#should get 3, 5, 6, 9
sum=0
for x in mult_3_5:
    sum+=x
print(sum)
#should get 23

#solution
mult_3_5=[]
i = 1
while i < 1000:
    if i%3==0 or i%5==0:
        mult_3_5.append(i)
    i += 1
sum=0
for x in mult_3_5:
    sum+=x
print(sum)