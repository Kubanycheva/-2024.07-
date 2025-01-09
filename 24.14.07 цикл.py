for i in range(4):
    print(i)
    i='Hello'
    print(i)


for i in range(4):
    print('liliya',i)
    print('cat', i)


for i in range(1000,10000):
    print(i)



for i in range(1, 11):
    print(i, i**2)



a = (input('Cоз жаз: '))
b = int(input('Сан жаз: '))
for i in range(b):
    print(a)


# a = input('write your name: ')
# for letter in a:
#     print(letter)



# numbers = [6, 7, 3, 2]
# for i in reversed(numbers):
#     print(i * 10)





# numbers = [6, 7, 3, 2]
# total = 0
# for i in numbers:
#     total += i
# print(total)







# numbers = [6, 7, 3, 2]
# max_number = 0 
# for i in numbers:
#     if max_number < i:
#         max_number = i  

# print(max_number)





# numbers = [6, 7, 3, 2]
# min_number = numbers[0]
# for i in numbers:
#     if min_number > i:
#         min_number = i 

# print(min_number)



# count = 0
# while count < 100: 
#     count += 10
#     print(count)

# total = 0
# while True:
#     number = int(input('number: '))
#     total += number

#     if number == 0:
#         print(f'summ == {total}')
#         break






# number = int(input('san jaz: '))

# for i in range(1, 11):
#     print(f'{i} * {number} = {i * number}')


# number = int(input('san jaz: '))

# for i in range(1, 11):
#     print(f' {i} * {number} = {i * number}')






# number = int(input('san jaz: '))
# print('Start')

# while number != -1:

#     print(number)
#     number -= 1
# print('The end')
    



# numbers = [3, 43, -54, -64, 7]
# new_list = []

# for i in numbers:
#     if i < 0:
#         new_list.append(i)
# print(new_list)




# one = int(input('1 san: '))
# two = int(input('2 san: '))
# total = 0
# for i in range(one, two):
#     total += i
# print(f'summa == {total}')




numbers = [4, 6, 2, 6, 7, 3, 1]

new_list = []
for i in numbers:
    if i % 2 != 0:
        new_list.append(i)
print(new_list)






# import random
# numbers = int(input('San jaz: '))
# numbers1 = int(input('San jaz: '))

# name = random.randint(numbers, numbers1)
# a = 0
# while True:
#     a += 1
#     f = int(input(f'{numbers} жана {numbers1} ортосундагы санды табыныз: '))
 
#     if  f > name:
#         print("Сиз жазган сан чон")
#     else:
#         print("Сиз жазган сан кичине")
#     if f == name:
#         print(f"Куттуктайбыз сиз {name} санын {a} иретте таптыныз.")
#         break 


# a = int(input('San jaz: '))
# print(f'Start')
# for i in reversed(range(a)):
#     print(i)
# print('The end')


# a = int(input('San jaz: '))
# print('Start')

# while a !=-1:
#     print(a)
#     a -=1
# print('The end')


