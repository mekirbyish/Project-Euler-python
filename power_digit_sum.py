#should be 32768, sum of each digit is 26
#a=pow(2,15)

a=pow(2,1000)
sum=0

#sum individual numbers in variable
for i in str(a):
    sum+=int(i)

print(sum)