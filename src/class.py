
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток:{self.quantity} "

    def __add__(self, other):
        if isinstance(other, Product):
            total_price = (self.price * self.quantity) + (other.price * other.quantity)
            total_quantity = self.quantity + other.quantity
            # Создаем новый объект Product с суммарной стоимостью и количеством
            return Product("Суммарный товар", total_price / total_quantity if total_quantity > 0 else 0, total_quantity)
        return NotImplemented

    @classmethod
    def new_product(cls, product_info: dict):
        """Создает новый объект Product из словаря с информацией о товаре."""
        name = product_info.get('name')
        price = product_info.get('price')
        quantity = product_info.get('quantity')

        if name is None or price is None or quantity is None:
            raise ValueError("Все параметры (name, price, quantity) должны быть указаны.")

        return cls(name, price, quantity)






class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения списка товаров




        Category.total_categories += 1

    def average_price(self):
        if not self.products:
            return 0  # Если товаров нет, возвращаем 0

        total_price = sum(product.price for product in self.products)
        total_quantity = sum(product.quantity for product in self.products)

        try:
            average = total_price / total_quantity
        except ZeroDivisionError:
            return 0  # Если сумма товаров равна 0, возвращаем 0

        return average

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)  # Добавляем продукт в список
            Category.total_products += 1  # Увеличиваем общее количество товаров
        else:
            raise ValueError("Только объекты класса Product могут быть добавлены.")

    def get_products(self):
        return self.__products[:]  # Возвращаем копию списка товаров для чтения

    def list_products(self):
        """Возвращает список товаров в формате: Название продукта, цена руб. Остаток: количество шт."""
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __repr__(self):
        return (f"Category(name={self.name}, description={self.description}, "
                f"total products={len(self.__products)})")

    def __str__(self):
        return f"{self.name}, количество продуктов:{self.description} "



class Smartphone(Product):
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.products = []

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты одного класса Product.")

        if self.__class__ is not other.__class__:
            raise TypeError("Нельзя складывать продукты разных типов.")

        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        total_quantity = self.quantity + other.quantity
        # Создаем новый объект Product с суммарной стоимостью и количеством
        return Product("Суммарный товар", total_price / total_quantity if total_quantity > 0 else 0, total_quantity)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников.")

        self.products.append(product)







class LawnGrass(Product):
    country: str
    germination_period: int
    color: str



product_data = {
    'name': 'Смартфон',
    'price': 0,
    'quantity': 0
}
product_data1 = {
    'name': 'Смартфон',
    'price': 0,
    'quantity': 0
}

product1 = Product.new_product(product_data1)

product_data2 = {
    'name': 'Планшет',
    'price': 300.00,
    'quantity': 3
}
product2 = Product.new_product(product_data2)
# Создаем новый продукт с помощью класса-метода
new_product = Product.new_product(product_data)

# Создаем категорию и добавляем продукт
electronics_category = Category(0, 0)
electronics_category.add_product(new_product)

# Вывод информации о категории с товарами
print(electronics_category)  # Вывод информации о категории
print(electronics_category.list_products())
total_product = product1 + product2
print(total_product)