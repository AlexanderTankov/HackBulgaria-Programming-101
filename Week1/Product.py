class Product():
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store():
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.sold_product = {}

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print(product.name, " - ", self.products[product])

    def sell_product(self, product):
        flag = False
        for items in self.products:
            if items == product and self.products[items] > 0:
                self.products[items] -= 1
                if items in self.sold_product:
                    self.sold_product[items] += 1
                else:
                    self.sold_product[items] = 1
                return True
        return flag

    def total_income(self):
        result = 0
        for stock in self.sold_product:
            if self.sold_product[stock] > 1:
                for price in range(0, self.sold_product[stock]):
                    result += stock.profit()
            else:
                result += stock.profit()
        return result


store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone)# True
store.sell_product(smarthphone)# True

print(store.total_income()) # 640