import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id': str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:

    def __init__(self, hotel):
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


class SpaHotel(Hotel):

    def book_spa_package(self):
        pass


class CreditCard:

    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_details = {'number': self.number, 'expiration': expiration, 'holder': holder, 'cvc': cvc}
        if card_details in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):

    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False


class Reservation:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name  # local variable
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you fo your resveration!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}            
"""
        return content


class SpaTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
           Thank you for your SPA reservation!
           Here are you SPA booking data:
           Name: {self.customer_name}
           Hotel name: {self.hotel.name}
           """
        return content


print(df)
hotel_id = input("Enter the id of the hotel: ")

hotel = SpaHotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number='1234')
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password='mypass'):
            hotel.book()
            name = input("Enter your name: ")

            reservation_ticket = Reservation(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())

            spa = input("Do you want to book a spa package? Enter 'yes' or 'no'")
            if spa == 'yes':
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel )
                print(spa_ticket.generate())
        else:
            print("Credit card authentication failed.")

    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free")







# str is also a class