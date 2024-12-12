import unittest
from app import Money, Dollar, Krw

class TestMoney(unittest.TestCase):
    def test_print_money(self):
        print(Money(1000, "Krw"))
    
    def test_money_initialization_not_in_locations(self):
        with self.assertRaises(ValueError):
            Money(1000, "adskljfsadjkl")
            
    def test_money_initialization(self):
        money = Money(1000, "Krw")
        self.assertEqual(money.holding_amount, 1000)
        self.assertEqual(money.location, "Krw")

    def test_decrease_or_increase(self):
        money = Money(1000, "Krw")
        money.decrease_or_increase(500)
        self.assertEqual(money.holding_amount, 1500)
        money.decrease_or_increase(-200)
        self.assertEqual(money.holding_amount, 1300)

    def test_exchange_krw_to_dollar(self):
        krw = Krw(1300)
        converted_amount = krw.exchange("Dollar")
        self.assertAlmostEqual(converted_amount, 1.0)
        
    def test_exchange_with_unsupported_location(self):
        money = Money(1000, "Krw")
        with self.assertRaises(ValueError) as context:
            money.exchange("InvalidCurrency")
        self.assertIn("Unsupported location", str(context.exception))

    def test_exchange_dollar_to_krw(self):
        usd = Dollar(1)
        converted_amount = usd.exchange("Krw")
        self.assertAlmostEqual(converted_amount, 1300)

if __name__ == "__main__":
    unittest.main()

'''
python -m unittest discover test
coverage run --source=app -m unittest discover test
coverage report or coverage report -m
'''