
# class Product:
#     def __init__(self, product_name, price, description, category, year):
#         self.product_name = product_name
#         self.price = price
#         self.description = description
#         self.category = category
#         self.year = year


#     def show(self):
#         return f'{self.product_name}, {self.price}, {self.description}, {self.category}, {self.year}'


# product1 = Product('Nike boots', 4000, 'fdsfdsafasd', 'shoes', 2020)
# print(product1.show()) 

# product2 = Product('Nike boots', 4000, 'fdsfdsafasd', 'shoes', 2020)


# class Computer:
#     def __init__(self, computer_name, price, description, category, year, model):
#         self.computer_name = computer_name
#         self.price = price
#         self.description = description
#         self.category = category
#         self.year = year
#         self.model = model

#     def show(self):
#         return f'{self.computer_name}, {self.price}, {self.description}, {self.category}, {self.year}. {self.model}'

# computer1 = Computer('Macbook', 400000, 'fdfsd', 'Laptop', 2022, 'Pro')
# print(computer1.show())

# computer2 = 'Macbook', 400000, 'fdfsd', 'Laptop', 2022, 'Pro'













# class Product:
#     def __init__ (self, name, price, description, category, year):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.category = category
#         self.year = year

#     def show(self):
#         return f'{self.name}, {self.price}, {self.description}, {self.category}, {self.year}'


# product1 = Product('Nike boots', 4000, 'fdsfdsafasd', 'shoes', 2020)
# print(product1.show())


# class Computer(Product):
#     def show(self):
#         return f'{self.name}, {self.price}, {self.description}, {self.category}, {self.year}'
# computer1 =Computer('Macbook', 400000, 'fdfsd', 'Laptop', 2022)
# print(computer1.show())#'Macbook', 400000, 'fdfsd', 'Laptop', 2022, 'Pro'













# class Product:
#     def __init__ (self, name, price, description, category, year):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.category = category
#         self.year = year

#     def show(self):
#         return f'{self.name}, {self.price}, {self.description}, {self.category}, {self.year}'


# product1 = Product('Nike boots', 4000, 'fdsfdsafasd', 'shoes', 2020)
# print(product1.show())


# class Computer(Product):

#     def init(self, name, price, description, category, year, model):
#         super().__init__ (name, price, description, category, year)
#         self.model = model

#     def show(self):
#         return f'{self.name}, {self.price}, {self.description}, {self.category}, {self.year}, {self.model}'
#         computer1 = Computer('Macbook', 400000, 'fdfsd', 'Laptop', 2022, 'Pro')
#         print(computer1.show())#'Macbook', 400000, 'fdfsd', 'Laptop', 2022, 'Pro'






# class Phone:
#     def __init__ (self, name, surname, age, floor):
#         self.name = name
#         self.price = surname
#         self.model = age
#         self.year = floor
#     def show(self):
#         return f'{self.name}, {self.price}, {self.model}, {self. year}'
    
# phone1 = Phone('Samsung', 'nokia', 18, 'female')
# print(phone1.show())
        

# class Car(Phone):
#     def __init__ (self, name, surname, age, floor, model):
#         super().__init__( name, surname, age, floor)
#         self.model = model

#     def show(self):
#         return f'{self.name}, {self.price}, {self.model}, {self.year}, {self.model}'

# car1 = Car('Camry', 14500, 'A', 2020, 'Pro')
# print(car1.show())  










# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def perimetr(self):
#         return f'{self.a + self.b * 2}'

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def perimtr(self):
#         return self.a + self.b + self.c
    
# tr1 = Triangle(4, 5, 2)
# print(tr1.perimtr())

# rec1 = Rectangle(4, 5)
# print(rec1.perimetr())


# def two_numbers(nums, t):
#     for i in nums:
#         numeric = t  -  i
#         if numeric in nums:
#             return [numeric, i]
        

# print(two_numbers([2, 4, 5, 8], 13))
# # [5, 8]4
