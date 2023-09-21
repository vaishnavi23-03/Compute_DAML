numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
n_x=len(numbers_x)
n_y=len(numbers_y)
if numbers_x[0]==numbers_x[n_x-1]:
    print("First and last value of x are equal")
else:
    print("First and last values of x are not equal")
if numbers_y[0]==numbers_y[n_y-1]:
    print("First and last values of y are equal")
else:
    print("First and last values of y are not equal")