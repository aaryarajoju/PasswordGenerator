import random

upperCaseLetters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCaseLetters: str = upperCaseLetters.lower()
digits: str = "0123456789"
symbols: str = "!@#$%^&*()_-+={[}]|\\/?.>,<;:"

upper: bool = True
lower: bool = True
nums: bool = True
syms: bool = True

allLetters: str = ""

if upper:
    allLetters += upperCaseLetters
if lower:
    allLetters += lowerCaseLetters
if nums:
    allLetters += digits
if syms:
    allLetters += symbols

length: int = 20
amount: int = 10

password: str

for x in range(amount):
    password = "".join(random.sample(allLetters, length))
    print(password)
