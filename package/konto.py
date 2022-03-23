"""Teil 1
Schreibe eine Klasse Konto mit einen Kontoinhaber, eine Kontonummer und einem Kontostand.
Der Name des Kontoinhabers soll geändert werden könnem, die Kontonummer aber nicht.

Schreibe eine Sub bzw. Kinderklasse Festgeldkonto, das kann mit einem gegebenen Zinssatz verzinst werden,
der Zinsatz soll für alle Festgeldkonten gleich sein.

Schreibe eine Sub bzw. Kinderklasse Girokonto (im Gegensatz zu allen anderen Konten), 
um einen bestimmten Betrag - den Dispokredit - überzogen werden kann.

Für alle drei Kontoarten sollen Einzahlungen möglich sein.

Für alle drei Kontoarten solen Abhebungen möglich sein.
Für ein normales Konto und ein Festgeldkonto können nur Beträge abgehoben werden, 
die kleiner als der Kontostand sind. Für ein Girokonto kann das Konto bis zu dem Betrag überzogen werden,
der durch Dispokredit festgelegt ist.

#########
## Exception
#########
Schreibe eine eigene Exception (Fehlerhandlung), die in dem Fall, dass auf dem Konto nicht genug Guthaben vorhanden ist.
geworfen wird und "ausgibt": Weil der Kontostand zu gering ist, kann keine Auszahlung gemacht werden.
Fange deine Exception in einem try/exception
 

Schreibe eine eigene Exception (Fahlerhandlung9, die in dem Fall, dass der Dispokredit überzogen wird,
geworfen wird und ausgibt "Sie haben Ihren Dsipokredit ausgeschafft")

"""


class BalanceLowExeption(Exception):
    def __str__(self) -> str:
        return super().__str__() + f"\nDie Auszahlung kann nicht durchgeführt werden.\n Versuchen Sie anderen Betrag!\n"


class DispokreditException(Exception):
    def __str__(self) -> str:
        return super().__str__() + f"Sie haben Ihren Dispokredit ausgeschöpft!"


class Konto:

    def __init__(self, kontoinhaber: str, kontonummer: str, kontostand: float) -> None:
        self.kontoInhaber = kontoinhaber
        self.__kontoNummer = kontonummer    # eine private Variable
        self.kontoStand = kontostand

    def __str__(self):
        return f"KontoInhaber: {self.kontoInhaber}\n Kontonummer: {self.getKontoNummer()}\n Kontostand: {self.getKontoStand()} Euroo \n"

    def setKontoInhaber(self, kontoinhaber: str):
        self.kontoInhaber = kontoinhaber

    def einzahlung(self, betrag):
        self.kontoStand += betrag

    def abhebung(self, betrag):
        if betrag < self.kontoStand:
            self.kontoStand -= betrag
        else:
            raise BalanceLowExeption()

    def getKontoStand(self):
        return f"{self.kontoStand:.2f}"

    def getKontoNummer(self) -> str:
        return self.__kontoNummer


class Festgeldkonto(Konto):
    def __init__(self, kontoinhaber: str, kontonummer: str, kontostand: float) -> None:
        super().__init__(kontoinhaber, kontonummer, kontostand)
        self.zinssatz = 0.05    # 5%

    def __str__(self):
        return super().__str__()

    def einzahlung(self, betrag):
        return super().einzahlung(betrag)

    def abhebung(self, betrag):
        return super().abhebung(betrag)

    def berechneZins(self):
        self.kontoStand *= (1 + self.zinssatz)


class Girokonto(Konto):
    def __init__(self, kontoinhaber: str, kontonummer: str, kontostand: float, dispoKredit: float) -> None:
        super().__init__(kontoinhaber, kontonummer, kontostand)
        self.dispoKredit = dispoKredit

    def __str__(self):
        return super().__str__() + f" Ihr Dispokredit: {self.dispoKredit} Euro\n"

    def einzahlung(self, betrag):
        return super().einzahlung(betrag)

    def abhebung(self, betrag):
        if betrag < (self.kontoStand + self.dispoKredit):
            self.kontoStand -= betrag
        else:
            raise DispokreditException()
