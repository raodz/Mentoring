import random

class Card:
    def __init__(self, value: str, color: str):
        self.value = value
        self.color = color

    def __str__(self):
        return f'{self.value} of {self.color}'

class Deck:
    def __init__(self):
        values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        colors = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        self.pile = []
        for value in values:
            for color in colors:
                self.pile.append(Card(value, color))

    def shuffle(self):
        random.shuffle(self.pile)

    def deal(self):
        last_card = self.pile[-1]
        self.pile = self.pile[:-1]
        return last_card

    def __str__(self):
        return str(self.pile)

def main():
    some_deck = Deck()
    print(some_deck)  # jak zrobić, żeby wyświetlały się nazwy kart?
    print(Card('3', 'Clubs'))
    print(some_deck.deal())
    some_deck.shuffle()
    print(some_deck)
    print(some_deck.deal())

if __name__ == '__main__':
    main()

