# number = int(input('Сан жаз: '))

# if number % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')



# name = str(input('Палидром жаз: '))

# if name == name[::-1]:
#     print('Palidrom')
# else:
#     print('Palidrom emes')


# age = input("Жашынды жаз: ")
# print(age)
# age = int(input('Жашынды жаз: '))
# if age > 18:
#     print('+ san')
# elif age < 18:
#     print('- san')
# else:       
#     print('== san')





# n = input('Напишите предложение: ')
# n1 = n.split()[-1]
# print(len(n1))





# n = int(input("Напишите число: "))
# if n % 2 == 0:
#     print('четное число')
# else:
#     print('нечетное число') 



# a = input('words: ').split()
# total = len(a[-1])
# print(f'создун узундугу {total}')
    
   


# number1 = (4, 6, 3, 7, 4)
# number2 = (5, 4, 2, 5, 3)
# n = number1 + number2
# # n1 = set(n)
# print(sorted(number1,reverse=True))



def find_numbers(nums, num):
    lists = []
    for i in nums:
        numbers = num - i
        if numbers in nums and nums != nums.index(i):
            list.append(i)
            list.append(numbers)
            if len(list) == 2:
                break
print(find_numbers([5, 6, 3, 4], 10))
[6, 4]