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


a = Bakery('R', -100, 1000)
b = Bakery('Bread', 1, 500)
print(a.get_name(), a.get_count_product(), a.get_avg_price())
print(b.get_name(), b.get_count_product(), b.get_avg_price())
