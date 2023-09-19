class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders_list = []
        self.customers_list = []
        
    def orders(self):
        return self.orders_list
    
    def customers(self):
        return self.customers_list
    
    def num_orders(self):
        return len(self.orders_list)
    
    def average_price(self):
        if len(self.orders_list) == 0:
            return 0
        else:
            prices_list = [order.price for order in self.orders_list]
            return sum(prices_list) / len(prices_list)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if (not hasattr(self, 'name')) and isinstance(name_parameter, str) and len(name_parameter) >= 3:
            self._name = name_parameter

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders_list = []
        self.coffees_list = []
        
    def orders(self):
        return self.orders_list
    
    def coffees(self):
        return self.coffees_list
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if type(name_parameter) == str and 1 <= len(name_parameter) <= 15:
            self._name = name_parameter
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        self.coffee.orders_list.append(self)

        if not (customer in self.coffee.customers_list):
            self.coffee.customers_list.append(customer)

        self.customer.orders_list.append(self)

        if not (coffee in self.customer.coffees_list):
            self.customer.coffees_list.append(coffee)

        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price_parameter):
        if (not hasattr(self, 'price')) and type(price_parameter) == float and 1.0 <= price_parameter <= 10.0:
            self._price = price_parameter

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer_parameter):
        if isinstance(customer_parameter, Customer):
            self._customer = customer_parameter

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee_parameter):
        if type(coffee_parameter) == Coffee:
            self._coffee = coffee_parameter
