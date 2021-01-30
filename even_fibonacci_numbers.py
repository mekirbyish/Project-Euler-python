fib_prev=0
fib_curr=1
fib_next=0
evens=[]
sum=0

#would be better as recursion
while fib_curr<4000000:
    #check if it's even
    if fib_curr%2==0:
        evens.append(fib_curr)
    fib_next=fib_prev+fib_curr
    fib_prev=fib_curr
    fib_curr=fib_next

#sum even fibs
for x in evens:
    sum+=x

print(sum)