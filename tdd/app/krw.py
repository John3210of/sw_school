from .money import Money

class Krw(Money):
    def __init__(self, holding_amount):
        super().__init__(holding_amount, "Krw")
