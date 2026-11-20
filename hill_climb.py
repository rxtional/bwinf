def main():
    # 1. initial state
    # 2. actions
    # 3. neighbors
    # 4. transition model
    # 5. evaluation
    # 6. goal state
    pass


def neighbors(state: object, all_projects: list):  # filtering the state out of the projects
    return [element for element in all_projects if element != state]
