class Card:
    values = {'6': 1, '7': 2, '8': 3, '9': 4, '10': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9}
    trump = None

    def __init__(self, val_suit):
        """
        accepts 2- or 3-symbol string:
        - first symbol is value (one of 678910JQKA)
        - second symbol is suit (one of CDHS)
        """
        self.val = val_suit[:-1]
        self.suit = val_suit[-1]

    def __gt__(self, other):
        if self.suit == other.suit:
            return self.values[self.val] > self.values[other.val]
        elif self.suit == self.trump:
            return True
        elif other.suit == self.trump:
            return False
        else:
            raise ValueError("Cannot compare different suits")

    def __eq__(self, other):
        return self.val == other.val and self.suit == other.suit


if __name__ == "__main__":
    card_strings = input().strip().upper().split()
    trump_suit = input().strip().upper()

    if len(card_strings) != 2 or len(trump_suit) != 1:
        print("2 cards are expected in first string, and 1 trump suit symbol is expected in the second string")
        exit(1)
    card1 = Card(card_strings[0])
    card2 = Card(card_strings[1])
    Card.trump = trump_suit
    winner = "Error"
    try:
        if card1 > card2:
            winner = "First"
        elif card2 > card1:
            winner = "Second"
    except ValueError:
        pass

    print(winner)