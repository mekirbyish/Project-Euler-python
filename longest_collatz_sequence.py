#want to have a recursive method, exist condition ==1
a=1
biggest_sequence=[]
test_sequence=[]

#iterative sequence as defined
def collatz_method(n):
    if n!=1:
        if n%2==0:
            n/=2
        else:
            n*=3
            n+=1
        test_sequence.append(n)
        collatz_method(n)

#find longest sequence under a million
while a < 1000000:
    test_sequence=[]
    test_sequence.append(a)
    collatz_method(a)
    if len(test_sequence)>len(biggest_sequence):
        biggest_sequence=test_sequence
    a+=1

print(biggest_sequence[0])
#print(biggest_sequence)