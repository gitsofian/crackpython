
from package.konto import *


konto = Konto('Sofiane', 'DE 49 1234 1234', 0.0)
print(konto)

girokonto = Girokonto('Julia', 'DE 49 3221 5432', 0.0, 200)
print(girokonto)

konto.einzahlung(1200.0)
print(konto)

girokonto.einzahlung(2000.0)
print(girokonto)

# Sofianes Konto
try:
    betrag = float(input('Sofiane, gib einen Betrag zur Abhebung : '))
    konto.abhebung(betrag)
except BalanceLowExeption as e:
    print(e)
else:
    print(f'\nAlles in Ordnung!')
finally:
    print(konto)
    print(f'\nOperation zum Ende!')


# Julias Konto
try:
    betrag = float(input('Julia, gib einen Betrag zur Abhebung : '))
    girokonto.abhebung(betrag)
except DispokreditException as e:
    print(e)
else:
    print(f'\nAlles in Ordnung!')
finally:
    print(girokonto)
    print(f'\nOperation zum Ende!')

# Julias Konto
try:
    betrag = float(input('Julia, gib einen Betrag zur Abhebung : '))
    girokonto.abhebung(betrag)
except DispokreditException as e:
    print(e)
else:
    print(f'\nAlles in Ordnung!')
finally:
    print(girokonto)
    print(f'\nOperation zum Ende!')
