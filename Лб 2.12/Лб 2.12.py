class Bakery():
    def __init__(self, name='', count_products=0, avg_price=0):
        self.__name = name
        self.__count_products = count_products
        self.__avg_price = avg_price

    def set_name(self, name):
        if type(name) in str:
            self.__name = name
        else:
            raise ValueError('Название пекарни должно иметь строковый тип')

    def set_count_products(self, count_products):
        if type(count_products) in int:
            self.__count_products = count_products
        else:
            raise ValueError('Количество изделий должно быть целым числом')

    def set_avg_price(self, avg_price):
        if type(avg_price) in (int, float):
            self.__avg_price = avg_price
        else:
            raise ValueError('Средняя цена на изделие должна быть либо целым,либо дробным числом')

    def get_name(self):
        return self.__name

    def get_count_product(self):
        return self.__count_products

    def get_avg_price(self):
        return self.__avg_price


a = Bakery('Игорь', 6, 1000)
b = Bakery('Кулеш', 1, 500)
# a.set_name('Кулеш')
print(a.get_name(), a.get_count_product(), a.get_avg_price())
print(b.get_name(), b.get_count_product(), b.get_avg_price())
