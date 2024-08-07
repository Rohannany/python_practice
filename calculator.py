
class Calculator:
    
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x/y
        else:
            return ("Cannot divide by zero")
        


calculator = Calculator()

print(calculator.add(3,5))