import sys


class Project:
    def __init__(self, votes):
        self.votes = votes
        self.donation_amount = 0

    def update_donation_amount(self, amount):
        self.donation_amount = amount


def main():
    validate_sys_arguments()
    file = read_file()


def validate_sys_arguments():
    if len(sys.argv) != 2:
        sys.exit("Use: python spendenaktion.py [file]")


def read_file():
    try:
        with open(f"Einlesedateien/{sys.argv[1]}", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        sys.exit("FNF: File not Found.")


def calculate_donation_amount(value, number_divisions):
    if value % 2 != 0:
        return value * 100

    return calculate_donation_amount(value // 2, number_divisions + 1)


if __name__ == "__main__":
    main()
