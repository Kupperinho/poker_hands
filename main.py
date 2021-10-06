import random
import pandas
from tkinter import *
import datetime as dt

# Card class that allow me to make deck of unique card


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit

# Function which is called after interacting with "deal_button". It makes deck, player hand,
# his position at the table and shows current efficient stacks


def new_hand():
    global hand, position, efficient_stacks

    table.delete("all")
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))
    random.shuffle(deck)

    hand = [deck.pop() for n in range(2)]
    positions = ["Btn", "BB", "SB"]
    position = random.choice(positions)
    efficient_stacks = random.randint(1, 25)
    table.create_text(200, 100, text=f"{hand[0]} {hand[1]}", fill="white", font=("helvetica", 15, "bold"))
    table.create_text(200, 125, text=f"pos: {position}   ES:{efficient_stacks}", fill="white", font=("helvetica", 15, "bold"))

# Function which save data after action


def save_choice(action):
    new_data = [[str(hand[0]), str(hand[1])], position, efficient_stacks, action]
    action_register.append(new_data)
    data = pandas.DataFrame(action_register, columns=["HAND", "POSITION", "STACKS", "ACTION"])
    data.to_csv(f"data/act_register[{date}].txt")
    new_hand()

# Setting data so every time user runs the app new register will be made


def set_data():
    now = dt.datetime.now()
    data_and_hour = f"{now.day}.{now.month}_{now.hour}-{now.minute}-{now.second}"
    return data_and_hour


action_register = []
hand = []
position = ""
efficient_stacks = 0

suits = ('♡', '♢', '♠', '♣')
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

date = set_data()

#   Interface

window = Tk()
window.title("Hand Dealer")
window.config(padx=20, pady=20)

table = Canvas(width=400, height=200, bg="green")
table.grid(row=0, column=0, columnspan=3, sticky="EW")

deal_button = Button(text="Deal", bg="brown", fg="white", command=new_hand)
deal_button.grid(row=1, column=0, sticky="EW")

min_raise = Button(text="MR", bg="brown", fg="white", command=lambda: save_choice("MR"))
min_raise.grid(row=1, column=1, sticky="EW")

all_in = Button(text="All-in", bg="brown", fg="white", command=lambda: save_choice("ALL-IN"))
all_in.grid(row=2, column=1, sticky="EW")

limp = Button(text="Call", bg="brown", fg="white", command=lambda: save_choice("LIMP"))
limp.grid(row=3, column=1, sticky="EW")

fold = Button(text="Fold", bg="brown", fg="white", command=lambda: save_choice("FOLD"))
fold.grid(row=1, column=2, sticky="EW")

new_hand()

window.mainloop()
