from src.command.menu import menu
from src.command.tracker import tracker
from src.command.total import total
from src.command.history import history


class command:
    def menu():
        return menu()

    def tracker(amount, type):
        return tracker(amount=amount, type=type)

    def total():
        return total()

    def history():
        return history()
