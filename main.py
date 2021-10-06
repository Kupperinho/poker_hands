import random
from tkinter import *

suits = ('♡', '♢', '♠', '♣')
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit


window = Tk()
window.title("Hand Dealer")

player_info = Canvas(window, width=300, height=300)
player_info.pack()


def show_hand():
    player_info.delete("label1")
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))
    random.shuffle(deck)


    hand = [deck.pop() for n in range(2)]
    positions = ["Btn", "BB", "SB"]
    random.shuffle(positions)

    label1 = Label(window, text=f'{hand[0]} {hand[1]} pos: {positions[0]} ES:{random.randint(1, 25)}', fg='green', font=('helvetica', 15, 'bold'))
    player_info.create_window(150, 200, window=label1)


deal_button = Button(text='Deal', command=show_hand, bg='brown', fg='white')
player_info.create_window(150, 150, window=deal_button)

window.mainloop()


