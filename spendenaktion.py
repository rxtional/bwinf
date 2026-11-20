class Project:
    def __init__(self, votes):
        self.votes = votes
        self.donation_amount = 0

    def update_donation_amount(self, amount):
        self.donation_amount = amount


def main():
    project = Project(24)
    project.update_donation_amount(calculate_amount(project.votes, 0))
    print(project.donation_amount)


def calculate_amount(value, number_divisions):
    if value % 2 != 0:
        return value * 100

    return calculate_amount(value // 2, number_divisions + 1)


if __name__ == "__main__":
    main()
