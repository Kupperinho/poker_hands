import random
import tkinter as tk

suits = ('♡', '♢', '♠', '♣')
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.size = "4x4cm"

    def __str__(self):
        return self.rank + self.suit


root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def show_board(label1=None):
    canvas1.delete("label1")
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))
    random.shuffle(deck)

    hand = [deck.pop() for n in range(2)]
    positions = ["Btn", "BB", "SB"]
    random.shuffle(positions)

    label1 = tk.Label(root, text=f'{hand[0]} {hand[1]} pos: {positions[0]} ES:{random.randint(1,25)}', fg='green', font=('helvetica', 15, 'bold'))
    canvas1.create_window(150, 200, window=label1)


button1 = tk.Button(text='Deal', command=show_board, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()


