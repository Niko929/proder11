class Exception_Value(Exception):
    name = 0
    price = 0
    quantity = 0


    def __init__(self, name, quantity,price):
        if price == 0:
          raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            print("0")
        self.name = name
        self.quantity = quantity
        self.price = price



try:
    product = Exception_Value( "dd", 0,0)
except ValueError as e:
    print(e)