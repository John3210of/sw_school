class Money:
    exchange_rates = {
        "Krw": 1,
        "Dollar": 1300
    }
    def __init__(self, holding_amount, location):
        if location not in self.exchange_rates:
            raise ValueError(f"Unsupported location '{location}")
        self.holding_amount = holding_amount
        self.location = location

    def decrease_or_increase(self, amount):
        self.holding_amount += amount
        
    def exchange(self, target_location) -> int:
        if target_location not in self.exchange_rates:
            raise ValueError(f"Unsupported location '{target_location}'. Available: {list(self.exchange_rates.keys())}")
        current_rate = self.exchange_rates[self.location]
        target_rate = self.exchange_rates[target_location]
        converted_amount = self.holding_amount * (current_rate / target_rate)
        return converted_amount

    def __repr__(self):
        return f"{self.__class__.__name__}(holding_amount={self.holding_amount}, location='{self.location}')"
    