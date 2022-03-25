

from package.pwManager import Account, AdminAccountException, AdminAcount


sap = Account('SAP', 'sofiane', 'Celle@@2022##')
sap.getProgrammName()
print(sap)


## hier würde ich sagen, wenn der Übergabeparameter isAdminAccount = False ist, dann würde ich ein Account 
try:
    sap.createAccount('Workday', 'Sofiane', '12121', isAdminAccount=False)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('SAP', 'Julia', '12121', isAdminAccount=True)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('Vscode', 'Redouane', '12121', isAdminAccount=True)
except AdminAccountException as e:
    print(e)

try:
    sap.createAccount('Sage', 'Hamid', '12121', isAdminAccount=False)
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

try:
    sap.createAccount('Sage', 'Niko', '12121')
except AdminAccountException as e:
    print(e)

## wenn der  Übergebeparameter isAdminAccount nicht gegeben wird,  
try:
    sap.createAccount('Sage', 'Nikolas', '12121')
except AdminAccountException as e:
    print(e)

sap.recapAccount()
