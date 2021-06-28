def square_numbers(nums):
    for i in range(nums):
        yield i**2


my_nums = square_numbers(5)
print(type(my_nums))

for num in my_nums:
    print(num)

