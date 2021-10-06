import random
from tkinter import *

#Card class that allow me to make deck of unique card

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit

#Function which is called after interacting with "deal_button". It makes deck, player hand,
#his position at the table and shows current efficient stacks

def new_hand():
    table.delete("all")
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))
    random.shuffle(deck)


    hand = [deck.pop() for n in range(2)]
    positions = ["Btn", "BB", "SB"]
    position = random.choice(positions)
    efficient_stacks = random.randint(1,25)
    table.create_text(200, 100, text=f"{hand[0]} {hand[1]}", fill="white", font=("helvetica", 15, "bold"))
    table.create_text(200, 125, text=f"pos: {position}   ES:{efficient_stacks}", fill="white", font=("helvetica", 15, "bold"))

suits = ('♡', '♢', '♠', '♣')
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

#   Interface

window = Tk()
window.title("Hand Dealer")
window.config(padx=20, pady=20)

table = Canvas(width=400, height=200, bg="green")
table.grid(row=0, column=0, columnspan=3, sticky="EW")

deal_button = Button(text="Deal", command=new_hand, bg="brown", fg="white")
deal_button.grid(row=1, column=0, sticky="EW")

min_raise = Button(text="MR", bg="brown", fg="white")
min_raise.grid(row=1, column=1, sticky="EW")

all_in = Button(text="All-in", bg="brown", fg="white")
all_in.grid(row=2, column=1, sticky="EW")

limp = Button(text="Call", bg="brown", fg="white")
limp.grid(row=3, column=1, sticky="EW")

fold = Button(text="Fold", bg="brown", fg="white")
fold.grid(row=1, column=2, sticky="EW")

new_hand()

window.mainloop()


