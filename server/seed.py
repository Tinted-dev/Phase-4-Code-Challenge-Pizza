#!/usr/bin/env python3

from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

with app.app_context():
    db.create_all()

    # Create some restaurants
    restaurant1 = Restaurant(name="Karen's Pizza Shack", address="123 Main St")
    restaurant2 = Restaurant(name="Sanjay's Pizza", address="456 Oak Ave")

    # Create some pizzas
    pizza1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Associate pizzas with restaurants
    restaurant_pizza1 = RestaurantPizza(price=10, restaurant=restaurant1, pizza=pizza1)
    restaurant_pizza2 = RestaurantPizza(price=15, restaurant=restaurant2, pizza=pizza2)

    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2, restaurant_pizza1, restaurant_pizza2])
    db.session.commit()

    print("Database seeded!")

