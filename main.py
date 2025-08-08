#imports that we need to make
# 1. import the get_crypto_price function
# 2. import the get_weather

from crypto import get_crypto_price
from weather import get_weather


def main():
    print(" Welcome to the API Tracker")
    choice = input("Type 'weather' or 'crypto': ")
    
    if choice == "weather":
        city = input("Enter city: ")
        get_weather(city)
    elif choice == "crypto":
        coin_id = input("Enter cryptocurrency: ")
        currency_id = input("Enter currency: ")
        get_crypto_price(coin_id, currency_id)
    else:
        print("Invalid choice")

# Only run this code when the file is run directly
# not when it's imported.
if __name__ == "__main__":
    main()