#should return 2640
#a=10

a=100
sum_squares=0
square_sums=0
i=1

#make list of numbers below limit, and another list of each's square summed
while i<=a:
    square_sums+=i
    sum_squares+=pow(i,2)
    i+=1

#square the sum of all the numbers below the limit
square_sums=pow(square_sums,2)

#find difference of these lists
difference=square_sums-sum_squares

print(difference)