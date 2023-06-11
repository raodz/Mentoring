class Menu:
    def __init__(self):
        pass

    def __str__(self):
        return '1. Add note\n' \
               '2. Add card\n' \
               '3. Show all notes\n' \
               '4. Show all cards\n' \
               '5. Exit'

    def get_choice(self):
        return input('Select an option')

class Submanager:
    def __init__(self, data = []):
        self.data = data

    def add(self, file):
        self.data.append(file)

    def __str__(self):
        return self.data

class Manager:
    def __init__(self, menu: Menu, notes_sm: Submanager, cards_sm: Submanager):
        self.menu = menu
        self.notes_sm = notes_sm
        self.cards_sm = cards_sm

    def start(self):
        pass  # jak ma działać start?

    def show_menu(self):
        return self.menu

    def execute(self):
        choice = self.menu.get_choice()