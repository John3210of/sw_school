from .money import Money

class Dollar(Money):
    def __init__(self, holding_amount):
        super().__init__(holding_amount, "Dollar")