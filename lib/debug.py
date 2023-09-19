#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer3 = Customer("Chris")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Starbucks")
    coffee3 = Coffee("Matcha Tea Latte")
    order1 = Order(customer1, coffee1, 30)
    order2 = Order(customer2, coffee2, 30)
    order3 = Order(customer1, coffee1, 40)

    ipdb.set_trace()
