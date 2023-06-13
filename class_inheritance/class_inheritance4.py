class Menu:
    def __str__(self):
        menu = (
            """
            1. Add note
            2. Add card
            3. Show all notes
            4. Show all cards
            5. Exit
            """
        )
        return menu
     # def show_choices -> print(menu)

    def get_choice(self):
        print(self)
        return input('Select an option')


class Submanager:
    def __init__(self, data):
        self.data = data or []

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
        # start

    def start(self):
        # show menu
        # execute
        pass  # jak ma działać start?

    def show_menu(self):
        return self.menu.__str__()

    def execute(self):
        choice = self.menu.get_choice()
        options = {
            '1': self.notes_sm.add,
            '2': self.cards_sm.add,
            '3': self.notes_sm.show,
            '4': self.cards_sm.show,
            '5': exit(),
        }
        if choice in options.keys():
            options.get(choice)
        else:
            print('Incorrect data')

        # print menu i get_choice

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
