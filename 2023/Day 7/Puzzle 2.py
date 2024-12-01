import operator

scores_of_cards = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14
}

hands = []
total_pay_out = 0

class Hand():
    def __init__(self, hand, bid):
        super().__init__()
        self.hand = hand
        self.bid = bid
        self.cards = []
        self.suits = []
        self.values = []
        self.score = 0
        self.set_score()
        self.set_values()

    def set_values(self):
        for card in self.hand:
            self.values.append(scores_of_cards[card])

    def set_score(self):
        card_count = {
            "A": 0,
            "K": 0,
            "Q": 0,
            "J": 0,
            "T": 0,
            "9": 0,
            "8": 0,
            "7": 0,
            "6": 0,
            "5": 0,
            "4": 0,
            "3": 0,
            "2": 0,
        }

        for card in self.hand:
            card_count[card] += 1

        joker_count = card_count["J"]
        card_count.pop("J")
        card_count[max(card_count.items(), key=operator.itemgetter(1))[0]] += joker_count


        for key in card_count:
            if card_count[key] == 5:
                self.score = 6
                break
            if card_count[key] == 4:
                self.score = 5
                break
            if card_count[key] == 3:
                if self.score == 1:
                    self.score = 4
                    break
                else:
                    self.score = 3
            if card_count[key] == 2:
                if self.score == 3:
                    self.score = 4
                    break
                elif self.score == 1:
                    self.score = 2
                    break
                else:
                    self.score = 1
        
    def __str__(self) -> str:
        return f"Hand: {self.hand}, Bid: {self.bid}, Score: {self.score}, Values: {self.values}"

    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            if self.values < other.values:
                return True
            else:
                return False
        else:
            return False

with open("2023/WWDay 7/data.txt") as f:
    for line in f:
        hands.append(Hand(line.split(" ")[0], line.replace("\n", "").split(" ")[-1]))

for i, hand in enumerate(sorted(hands)):
    total_pay_out += int(hand.bid) * (i + 1)

print(total_pay_out)
