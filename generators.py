# https://www.youtube.com/watch?v=bD05uGo_sVI

# standard
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums)

def square_numbers(nums):
    result = []
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

