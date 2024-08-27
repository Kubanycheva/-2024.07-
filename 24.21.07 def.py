
# def new_numbers(numbers1, numbers2):
#     new_list = numbers1 + numbers2
#     new_list = sorted(new_list, reverse=True)
#     return new_list
# print(new_numbers([4, 6, 1], [5, 9, 2]))


def remove_duplicates(a):
    a = sorted(set(a))
    return a
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    
# def age(year_born, cor_year):
#     return cor_year - year_born
# print(age(2006, 2026))



# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# is_prime_number = 2
# print(is_prime(is_prime_number))  

# is_not_prime_number = 4
# print(is_prime(is_not_prime_number))  




# def change_numbers(numbers):
#     new_list = []
#     for num in numbers:
#         if num == 4:
#             new_list.append(0)
#         elif num == 5:
#             new_list.append(num)
#         elif num == 2:
#             new_list.append(num * 2)
#         elif num == 7:
#             new_list.append(num * 3)
#         elif num == 8:
#             new_list.append(num * 4)
#     return new_list
# print(change_numbers([4, 5, 2, 7, 8]))




# def check_numbers(a):
#     if a % 2 == 0:
#         return 'Jup san'
#     else:
#         return 'Tak san'
# print(check_numbers(5))











# person = {'last_name': 'Asel', 'age': 33, 'number': 3543543}

# def check_key(word):
#     if word in person:
#         return person[word]
#     else:
#         return 'Jok'

# print(check_key('dfgdfg'))


# def check_numbers (numbers):
#     return[]
# print(check_numbers([5, 3, -5, 3, -7, -3, 1, -8]))




# def check_numbers(numbers):
#     new_list = []
#     for i in numbers:
#         if i > 0:
#             new_list.append(i)
#         else:
#             new_list.append(0)
#     return new_list
# print(check_numbers([5, 3, -5, 3, -7, -3, 1, -8]))




# def change_number(numbers):
#     new_list = []
#     for i in numbers:
#         if i % 5 == 0:
#             new_list.append(i * 5)
#         elif i % 3 == 0:
#             new_list.append(i * 3)
#         else:
#             new_list.append(i)
#     return new_list

# print(change_number([5, 2, 7, 6, 10, 0, 12]))

# [25, 2, 7, 18, 50, 0, 36]


