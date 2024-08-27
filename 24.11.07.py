# a = input('word1: ')
# b = input('word2: ')

# if sorted(a) == sorted(b):
#     print('Anagramma')
# else:
#     print('Anagramma emese')

  

# numbers = [53, 6, 46, 4]
# if  min(numbers) > 0:
#     print('-San jok')
# else:
#     print('-San bar')


# cars = {'car_name': 'mers', 'model': 'AMG', 'price': 50000}
# word = input('write a key: ')

# if word in cars:
    
#     print(cars[word])
# else:
#     print('Error')



# cars = {'car_name': 'mers', 'model': 'AMG', 'price': 50000}
# word = input('write a key')




# numbers = (1, 2, 3)
# letters = ("a", "b", "c")




# word = str(input('Palidrom jaz: '))
# if word == word[::-1]:
#     print('Palidrom')
# else:
#     print('Palidrom emes')






# cars1 = ['byd', 'mers', 'audi', 'bmw', 'honda', 'tesla']
# cars2 = ['mers', 'matiz', 'audi', 'honda', 'tesla']

# new_cars1 = set(cars1)
# new_cars2 = set(cars2)
# count_cars = new_cars1.intersection(new_cars2)

# print(f'окшош машиналардын саны {len(count_cars)}')





# a = {'a': 100, 'b': 400} 
# b = {'c': 400, 'd': 600}
# numbers_dict = {**a, **b}
# print(numbers_dict)







# print("I'm", "the", "BAD", "guy")

# print('Как тебя зовут?')     

# print('Привет,', input())

# name = input()
# print('Привет,', name)


# print('Как тебя зовут?')
# name = input()


# name = input()
# print('I am', name, '!')

# name1 = input()
# print('I am', name1, '.')



# print('Какой язык программирования ты изучаешь?')

# language = input()

# print(language, '- отличный выбор!')


# a = input()
# b = input()
# c = input()
# print(c)
# print(b)
# print(a)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)


# a = [1, 2, 2, 3, 4, 4, 5]
# b = sorted(set(a))
# print(b)


# n = int(input("Напишите число: "))
# if n % 2 == 0:
#     print('четное число')
# else:
#     print('нечетное число') 





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






# is_prime_number = 7  

# # Проверка на простое число
# if is_prime_number <= 1:
#     result = False
# elif is_prime_number <= 3:
#     result = True
# elif is_prime_number % 2 == 0 or is_prime_number % 3 == 0:
#     result = False
# else:
#     i = 5
#     result = True
#     while i * i <= is_prime_number:
#         if is_prime_number % i == 0 or is_prime_number % (i + 2) == 0:
#             result = False
#             break
#         i += 6

# print(result)  








