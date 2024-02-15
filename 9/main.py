from classes import Product, Warehouse


product1 = Product("Молоко", 10, 50)
product2 = Product("Хлеб", 20, 30)
product3 = Product("Яйца", 50, 5)

# Добавление продуктов на склад
warehouse = Warehouse()
warehouse.add_product(product1)
warehouse.add_product(product2)
warehouse.add_product(product3)

# Вывод информации о продуктах на складе
warehouse.print_products()

# # Обновление информации о продукте
warehouse.update_product("Хлеб", quantity=25, price=None)
#
# # Вывод обновленной информации о продуктах на складе
warehouse.print_products()
#
# # Подсчет общей стоимости продуктов на складе
total_value = warehouse.calculate_total_value()
print("Общая стоимость продуктов на складе:", total_value)