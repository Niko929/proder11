
class Exception_Value(Exception):


    def __init__(self, name, quantity):
        if quantity <= 0:
          raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.quantity = quantity


try:
    product = Exception_Value("Товар1", 0)
except ValueError as e:
    print(e)