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
        print(self)
        return input('Select an option')

class Submanager:
    def __init__(self, data = []):
        self.data = data

    def add(self):
        file = input('Type the file to add')
        self.data.append(file)

    def show(self):
        print(self.data)

class Manager:
    def __init__(self, menu: Menu, notes_sm: Submanager, cards_sm: Submanager):
        self.menu = menu
        self.notes_sm = notes_sm
        self.cards_sm = cards_sm

    def start(self):
        pass  # jak ma działać start?

    def show_menu(self):
        return self.menu.__str__()

    def execute(self):
        options = {'1': self.notes_sm.add, '2': self.cards_sm.add,
                   '3': self.notes_sm.show, '4': self.cards_sm.show}
        choice = '1'  # to tylko wartość początkowa
        while choice != '5':
            choice = self.menu.get_choice()
            if choice in ['1', '2', '3', '4']:
                options[choice]()
            elif choice == '5':
                print('Thank you for using the program')
            else:
                print('Please provide correct option: 1, 2, 3, 4 or 5')

def main():
    menu = Menu()
    notes_sm = Submanager()
    cards_sm = Submanager()
    manager = Manager(menu, notes_sm, cards_sm)
    manager.start()  # co to ma robić?
    manager.show_menu()
    manager.execute()
# problem: 1 i 2 dodają elementy do listy tego samego Submanagera

if __name__ == '__main__':
    main()