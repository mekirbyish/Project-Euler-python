a=100
b=100
d=0
x=0

#tests if all numbers up to limit are palindroms
while a<1000:
    z=b
    while b<1000:
        c=a*b
        if str(c)==str(c)[::-1]:
            d=int(c)
            if d>x:
                x=d
        b+=1
    b=z+1
    a+=1

print(x)