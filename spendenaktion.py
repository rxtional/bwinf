class Projekt:
    def __init__(self, stimmen):
        self.stimmen = stimmen
        self.spendenbetrag = 0

    def aktualisiere_spendenbetrag(self, betrag):
        self.spendenbetrag = betrag

        return betrag


def main():
    # test
    projekt = Projekt(stimmen=64)
    betrag = berechne_betrag(projekt.stimmen, 0)
    projekt.aktualisiere_spendenbetrag(betrag)
    print(projekt.spendenbetrag)


def berechne_betrag(wert, anzahl_teilungen):
    """
    Berechnet, wie oft man eine Zahl durch 2 teilen kann und multipliziert das Ergebnis mit 100.
    """
    if wert % 2 != 0:
        return anzahl_teilungen * 100

    return berechne_betrag(wert // 2, anzahl_teilungen + 1)


if __name__ == "__main__":
    main()
