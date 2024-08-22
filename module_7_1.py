from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        for line in file:
            print(line.strip())
        file.close()

    def add(self, *products):
        self.products = products
        for prod_ in self.products:
            with open('products.txt', 'r') as file:
                lines = file.read()
                if f'{prod_}' in lines:
                    print(f'Продукт {prod_} уже есть в магазине')
                    file.close()
                else:
                    with open('products.txt', 'a+') as file:
                        file.write(f'{prod_}\n')
                        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())