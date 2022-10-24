# Use map() function with explicit function
def fahrenheit(cel):
    return (9/5)*cel + 32

#Lambda function
celsius_list = [0, 37, 80, 100]
fah_list = list(map(fahrenheit, celsius_list))
print(fah_list)

f = lambda x, y: x + y # : return x+y
print(f(1, 4))

# map function with lambda function
celsius_list = [0, 37, 80, 100]
fah_list = list(map(lambda c: (9/5)*c + 32, celsius_list)) # return (9/5)*c + 32, celsius_list
print(fah_list)

#filterfilterfilter
#filter with explicit function
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
fib_even_list = list(filter(is_even, fib_list))
print(fib_even_list)

# filter() with lambda function
fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
fib_even_list = list(filter(lambda x: x%2 == 0, fib_list))
print(fib_even_list)

# filter with list comprehension
fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
fib_even_list = [x for x in fib_list if x%2 == 0]
print(fib_even_list)
