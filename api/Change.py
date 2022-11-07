# ChangeEngine.py
# Description: Helper class, it creates a Change object which holds change information

class Change:
    def __init__(self,change):
        self.change = change

    def get_total(self):
        total = 0
        for coin, amount in self.change.items():
            total+= coin*amount
        return total

    def get_change(self):
        return self.change