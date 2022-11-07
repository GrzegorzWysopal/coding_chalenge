# main.py
# Description: CMD line program to test API functionality.

import os
import config
from api.ChangeEngine import ChangeEngine

def main():
    clear_console()
    change_client = ChangeEngine(config.initial_coins)
  
    while True:
        display_product_offering()

        # Validate input
        while True:
            try:    
                product = int(input("Please select a number: \n"))
                if product not in config.menu.keys():
                    print("The product with this number does not exist, please try again")
                else:
                    to_pay = config.menu[product][1]
                    break
            except Exception:
                clear_console()
                print("!!! Wrong input, please use only whole numbers from the menu !!!\n")
                display_product_offering()
        clear_console()

        # Product choise approved, continue...

        display_balance(product, to_pay, change_client.get_user_balance())  
        while to_pay > change_client.get_user_balance():
            try:
                coin = float(input("Please insert a coin... "))
                change_client.insert_coin(coin)

                if change_client.get_user_balance() >= to_pay:
                    change = change_client.return_change(to_pay)
                    break
                else:
                    clear_console()
                    display_balance(product, to_pay, change_client.get_user_balance()) 
            except Exception:
                clear_console()
                print(f"Wrong input" + 
                      f"Accepted coins are: {', '.join(map(str,change_client.get_coins_denomination()))} .")
        clear_console()

        # Change calculation finished, continue...
   
        if change[1] == False:
            print("Not enough coins in the machine\n" +
                "Giving back your deposit: " +
                "Coins received: ")
            print(f" ___________")
            for coin,amount in change[0].get_change().items():
                position = f"|{coin} - {amount}x"
                print(position + " " *(12 - len(position)) + "|" )
            print(f" ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
        else:
            print(f"Your change: {change[0].get_total():.2f} £")
            print()
            print("Coins received: ")
            print(f" ___________")
            for k,v in change[0].get_change().items():
                position = f"|{k} £ - {v}x"
                print(position + " " *(12 - len(position)) + "|" )
            print(f" ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
            print("Thank you for shopping !\n")

        cont = input("Press Enter to continue...")
        clear_console()
        

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_product_offering():
    print("Welcome to the vending machine \n" +
          "Please select a product from the list:\n")     
    print(f" ________________________________________________")
    for product in config.menu:
        position = f"| Number: {product} | Name: {config.menu[product][0]}" + " "*(12-len(config.menu[product][0])) + f" | Price: {config.menu[product][1]} £"
        print(position + " " *(48 - len(position)) + " |" )
    print(f" ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻\n")

def display_balance(product, to_pay, balance):
    print(f"\nYour choice: {config.menu[int(product)][0]}\n" +
          f"Your current balance is: {balance:.2f} £\n" + 
          f"You need {to_pay-balance:.2f} £ more to pay\n")


if __name__ == '__main__':
    main()