

from package.pwManager import Account, AdminAccountException, AdminAcount


sap = Account('SAP', 'sofiane', 'Celle@@2022##')
sap.getProgrammName()
print(sap)



try:
    sap.createAccount('Workday', 'Sofiane', '12121', False)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('SAP', 'Julia', '12121', True)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('Vscode', 'Redouane', '12121', True)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('Sage', 'Hamid', '12121', False)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('Sage', 'Viktoria', '12121', False)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('Sage', 'Niko', '12121', True)
except AdminAccountException as e:
    print(e)

sap.recapAccount()
