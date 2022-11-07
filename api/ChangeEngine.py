# ChangeEngine.py
# Description: Holds main logic of Change engine


import math
import api.Change as Change
import api.Statics as Statics
from collections import defaultdict

class ChangeEngine:
    def __init__(self, init_coins: dict):
        self.__coins_inside_machine = self.__validate(init_coins)
        self.__user_balance = 0.00

    def __validate(self,coins: dict) -> None:
        error_msg = "Wrong input, not initialised! Expected 'dict' reflecting static.available_coins !" 
        if [*coins] == Statics.available_coins:
            for value in coins.values():
                if not isinstance(value, int) or value < 0:
                    raise TypeError(error_msg)
            return coins
        else:
            raise TypeError(error_msg)

    def return_change(self, product_price: float):
        if product_price < 0:
            raise Exception("'product_price' must be positive")
        try:
            change = self.__user_balance - round(product_price,2)
        except Exception:
            raise TypeError(f"'product_price' must be a number not {type(product_price)}")
        if change < 0:
            raise Exception(f"Not enough coins deposited by the user, can not return change")

        payment_recieved = self.__user_balance
        change_distribution = defaultdict(lambda:0)

        for coin in Statics.available_coins:
            while coin < change and self.__coins_inside_machine[coin] > 0 or math.isclose(coin,change) and self.__coins_inside_machine[coin] > 0 :
                change-= coin
                change_distribution[coin]+=1

        if change > min(Statics.available_coins):
            self.__user_balance = payment_recieved
            give_back_deposit = self.return_change(0)
            give_back_deposit[1] = False
            return give_back_deposit
        else:
            for key, value in change_distribution.items():
                self.__coins_inside_machine[key]-= int(value)
            self.__user_balance = 0.00
            return [Change.Change(change_distribution),True]

    def insert_coin(self, coin: float):
            if coin in Statics.available_coins:
                self.__user_balance+=coin
                self.__coins_inside_machine[coin]+=1
            else: 
                raise TypeError(f"Coin argument must be a number of value: {', '.join(map(str,Statics.available_coins))}")

    def get_user_balance(self):
        return self.__user_balance
    
    def get_coins_status(self):
        return self.__coins_inside_machine

    def get_coins_denomination(self):
        return Statics.available_coins






        




