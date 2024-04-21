class Bakery():
    def __init__(self, name:str, count_products:int, avg_price: (int, float)):
        self._name = name
        self._count_products = count_products
        self._avg_price = avg_price

    def set_name(self, name:str):
        self._name = name

    def set_count_products(self, count_products:int):
        self._count_products = count_products

    def set_avg_price(self, avg_price:(int,float)):
        self._avg_price = avg_price

    def get_name(self):
        return self._name

    def get_count_product(self):
        return self._count_products

    def get_avg_price(self):
        return self._avg_price


a = Bakery(6, 100, 1000)
b = Bakery('Кулеш', 1, 500)
print(a.get_name(), a.get_count_product(), a.get_avg_price())
print(b.get_name(), b.get_count_product(), b.get_avg_price())
# a.set_name('Кулеш')