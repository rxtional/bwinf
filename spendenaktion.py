class Projekt:
    def __init__(self, stimmen):
        self.stimmen = stimmen
        self.spendenbetrag = 0

    def berechne_spendenbetrag(self, stimmenwert, anzahl_teilungen):
        if stimmenwert % 2 != 0:
            spendenbetrag = anzahl_teilungen * 100

            self.spendenbetrag = spendenbetrag
            return spendenbetrag
        return self.berechne_spendenbetrag(
            stimmenwert=stimmenwert/2, anzahl_teilungen=anzahl_teilungen+1)


def main():
    # test
    projekt = Projekt(stimmen=80)
    print(
        f"[db] spendenbetrag projekt: {projekt.berechne_spendenbetrag(stimmenwert=projekt.stimmen, anzahl_teilungen=0)}")


if __name__ == "__main__":
    main()
