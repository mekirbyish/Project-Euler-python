#fib_start_1=1
#fib_start_2=2
#print(fib_start_1)
#print(fib_start_2)
fib_prev=0
fib_curr=1
fib_next=0
evens=[]
sum=0
while fib_curr<4000000:
    #print(fib_curr)
    if fib_curr%2==0:
        evens.append(fib_curr)
    fib_next=fib_prev+fib_curr
    fib_prev=fib_curr
    fib_curr=fib_next
for x in evens:
    sum+=x
print("sum is ",sum)