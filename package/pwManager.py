

"""
Schreibe eine Klasse Account mit den drei Attributen
program - das Programm, zu dem der Account gehört
username - der Benutzername, der zum Zugang zu dem Programm verwendet wird
password - das Password, das zum Zugang zu dem Programm verwendet wird
und zwei Methoden/Funktionen:
getProgramName() - die das zugehörige Programm des Accounts zurück gibt
changePassword(password) - um das gespeicherte Password zu ändern


"""


class AdminAccountException(Exception):
    def __str__(self) -> str:
        return super().__str__() + f"Es dart nur ein Admin Account!\n"

class Account:
    def __init__(self, program: str, username: str, password: str) -> None:
        self.__program: str = program
        self.__username: str = username
        self.__password: str = password
        self.__hatAdminAccount: bool = False
        self.__accounts: AdminAcount = []
        
    def __str__(self) -> str:
        return f"Acoount: {self.__username} fürs Programm {self.__program} würde erfolgreich erstellt"
    
    def recapAccount(self):
        for acc in self.__accounts:
            print(f"Program: {acc.__program}\n Username: {acc.__username}\n Password: {acc.__password}\n isAdminAccount: {acc.isAdminAccount()}\n")
        print(f"Insgesamte Account würde erstellt: {len(self.__accounts)}")
    
    def getProgrammName(self) -> str:
        return self.__program
    
    def setProgrammName(self, program) -> bool:
        self.__program = program
    
    def __getPassword__(self) -> str:
        return self.__password
    
    def __setPassword__(self, password) -> bool:
        self.__password = password
        return True
    
    def changePassword(self, password) -> bool:
        oldPassword = self.__getPassword__()
        
        if oldPassword != password:
            self.__setPassword__(password)
            print(f"Password würde erfolgreich geändert\n")
            return True   
        else:
            print(f"Das Password würde nicht geändert!\n")
            return False
   
    def __setUsername__(self, username):
        self.__username = username
        
    def __getUsername__(self) -> str:
        self.__username
    
    def __getAdminAcount__(self):
        return self.__hatAdminAccount
    
    def __setAdminAccount__(self):
        self.__hatAdminAccount = True
            
    def createAccount(self, program: str, username: str, password: str, isAdminAccount = False):
        if not isAdminAccount:  ### ein UserAccount würde erstellt
            acc = AdminAcount(program, username, password, isAdminAccount)
            self.__accounts.append(acc)
        else:
            if not self.__getAdminAcount__():
                acc = AdminAcount(program, username, password, isAdminAccount)
                self.__accounts.append(acc)
                self.__setAdminAccount__()
            else:
                raise AdminAccountException()
    

"""
Schreibe eine Klasse AdminAccount, die von Account erbt.
AdminAccount hat ein zusätzliches Attribut istAdminAccount - boolean
Überlege dir, wie man den AdminAccount besonders gegen die Manipulierung
von Daten schützen sollte.
Es dart nur ein AdminAccount erstellt werden
Überlege dir, wie man die erstellung eines weiteren AdminAccount verhindern könnte - Exception!

"""  
class AdminAcount(Account):
    def __init__(self, program: str, username: str, password: str, isAdminAccount: bool) -> None:
        super().__init__(program, username, password)
        self.__isAdminAccount: bool = isAdminAccount
        
    def __str__(self) -> str:
        msg = 'Admin Account würde erfolgreich ergestellt!' if self.isAdminAccount else 'User Account würde erfolgreich ergestellt!'
        return super().__str__() + f"\n"
    
    def isAdminAccount(self) -> bool:
        return self.__isAdminAccount
