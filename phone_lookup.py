import os
from twilio.rest import Client

from twilio.base.exceptions import TwilioRestException

# Replace these values with your Twilio account SID and auth token
account_sid = 'enter your sid here'
auth_token = 'enter your auth token here'

client = Client(account_sid, auth_token)


def perform_reverse_lookup(phone_number):
    try:
        number = client.lookups.v1.phone_numbers(phone_number).fetch(type=['carrier'])
        carrier = number.carrier
        return carrier
    except TwilioRestException as error:
        return None
def main(): 
    phone_number = input("Which phone number would you like to search? ")
    reverse_lookup_choice = input("Do you want to perform a reverse lookup and see any relevant data? (y/n) ")

    if reverse_lookup_choice.lower() == 'y':
        carrier = perform_reverse_lookup(phone_number)
        if carrier:
            print(f"Phone number: {phone_number}")
            print(f"Carrier: {carrier['name']}")

            with open("phone_number_data.txt", "w") as file:
                file.write(f"Phone number: {phone_number}\n")
                file.write(f"Carrier: {carrier['name']}\n")
            print("Data saved in phone_number_data.txt")
        else:
            print("No data found for the given phone number.")

if __name__ == "__main__":
    main()
