from ..fees import apply_fee
from ..account import show_balance
from .calculator import deposit




balance = 1000

print(show_balance(balance))

balance = deposit(balance, 500)
print(show_balance(balance))

balance = apply_fee(balance, 50)
print(show_balance(balance))

