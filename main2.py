from abc import ABC, abstractmethod

import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id': str})


class Hotel:
    # class variable: are coded outside the method

    # """ this can be shared across all instances """
    watermark = "The real estate company"

    def __init__(self, hotel):
        # instance variable :- are coded inside the method
        self.hotel = hotel
        self.name = df.loc[df['id'] == hotel, 'name'].squeeze()

    def available(self):
        """check if the hotel is available"""

        availability = df.loc[df['id'] == self.hotel, 'available'].squeeze()
        return availability == 'yes'

    def book(self):
        """ book a hotel by changing its availability to no """
        df.loc[df['id'] == self.hotel, 'available'] = 'no'
        df.to_csv("hotels.csv", index=False)

    # Class Method
    # decorator

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)


class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass

# if any class inherit abstract class then all abstract method must be inherited
# used when child class must have all method of parent class


class Reservation(Ticket):

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you fo your resveration!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}            
"""
        return content

    # Properties: instance method
    # we do not need to call this method , it behaves as a variable
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()         # local variable
        name1 = name.title()
        return name1

    # static method : use for utility
    @staticmethod
    def convert(amount):
        return amount * 1.2

    # magic method
    # Hotel.__eq__(hotel1, hotel2)
    def __eq__(self, other):
        if self.hotel == self.hotel:
            return True
        else:
            return False

# hotel1 = Hotel(hotel='188')
# hotel2 = Hotel(hotel='134')
#
# # self holds the value of hotel1 instance
#
# print(hotel1.name)
# print(hotel2.name)
#
# print(hotel1.watermark)
#
# print(Hotel.watermark)
#
#
# # instance method : can be applied to instance
# print(hotel1.available())
#
# print(Hotel.get_hotel_count(data=df))
# print(hotel1.get_hotel_count(data=df))
#
#
# # Instance Attribute :- """ instance variables, instance methods"""
# # Class Attribute :- """ class variables, class methods"""
#
#
# ticket = Reservation(customer_name='john smith ', hotel_object=hotel1)
# print(ticket.the_customer_name)
#
#
# converted = Reservation.convert(amount=10)
# print(converted)


# h == h
# == is syntactic sugar which is simplified syntax
# __eq__


# every instance is different even if they have ths same argument
