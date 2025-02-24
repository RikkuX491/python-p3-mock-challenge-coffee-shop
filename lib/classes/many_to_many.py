class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def coffee_name_getter(self):
        return self._name
    
    @coffee_name_getter.setter
    def name(self, name_value):
        if (not hasattr(self, 'name')) and (type(name_value) == str) and (len(name_value) >= 3):
            self._name = name_value
        
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if self.num_orders() == 0:
            return 0
        else:
            price_list = [order.price for order in self.orders()]
            return sum(price_list) / len(price_list)

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, name_value):
        if (type(name_value) == str) and (1 <= len(name_value) <= 15):
            self._name = name_value
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if (type(value) is float) and (not hasattr(self, 'price')) and (1.0 <= value <= 10.0):
            self._price = value

    @property
    def customer_getter(self):
        return self._customer
    
    @customer_getter.setter
    def customer(self, value):
        if type(value) == Customer:
            self._customer = value

    @property
    def coffee_getter(self):
        return self._coffee
    
    @coffee_getter.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value