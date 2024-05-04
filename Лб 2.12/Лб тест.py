class Bakery():
    def __init__(self, name: str, count_products: int, avg_price: (int, float)):
        self.set_name(name)
        self.set_count_products(count_products)
        self.set_avg_price(avg_price)

    def set_name(self, name: str):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Тип имени должен быть строковым.")

    def set_count_products(self, count_products: int):
        if isinstance(count_products, int) and count_products >= 0:
            self.count_products = count_products
        else:
            raise ValueError("Количество изделий должно быть целым числом и положительным.")

    def set_avg_price(self, avg_price: (int, float)):
        if isinstance(avg_price, (int, float)) and avg_price >= 0:
            self.avg_price = avg_price
        else:
            raise ValueError("Средняя цена на изделие должна быть либо целым,либо дробным числом и больше 0.")

    def get_name(self):
        return self.name

    def get_count_product(self):
        return self.count_products

    def get_avg_price(self):
        return self.avg_price


a1 = Bakery('Bread', 2400, 5000)
a2 = Bakery('Fish', 30, 100000)
a3 = Bakery('Gold', 100, 1000)
a4 = Bakery('Happy', 1100, 1000)
a5 = Bakery('Sun', 1100, 10000)
a6 = Bakery('1', -5100, 10)
print(a1.get_name(), a1.get_count_product(), a1.get_avg_price())
print(a2.get_name(), a2.get_count_product(), a2.get_avg_price())
print(a3.get_name(), a3.get_count_product(), a3.get_avg_price())
print(a4.get_name(), a4.get_count_product(), a4.get_avg_price())
print(a5.get_name(), a5.get_count_product(), a5.get_avg_price())
print(a6.get_name(), a6.get_count_product(), a6.get_avg_price())

