sum_squares=0
square_sums=0
i=1
while i<=100:
    square_sums+=i
    sum_squares+=pow(i,2)
    i+=1
square_sums=pow(square_sums,2)
difference=square_sums-sum_squares
print(difference)