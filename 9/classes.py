class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Warehouse:

    def __init__(self):
        self.warehouse = dict()

    def add_product(self, product):
        self.warehouse[product.name] = product

    def print_products(self):
        for product_name, product in self.warehouse.items():
            print(f'Продукт: {product.name}')
            print(f'Количество: {product.quantity}')
            print(f'Цена за единицу: {product.price}\n')

    def update_product(self, name, quantity=None, price=None):
        if name in self.warehouse:
            if quantity:
                self.warehouse[name].quantity = quantity
            if price:
                self.warehouse[name].price = price

            print("Обновленная информация:\n")

    def calculate_total_value(self):
        return sum(product.price * product.quantity for product in self.warehouse.values())
