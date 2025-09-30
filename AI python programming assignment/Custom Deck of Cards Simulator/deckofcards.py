import random
from collections import Counter

def simulate_deck(output_file, n=5):
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    drawn = deck[:n]
    suit_counts = Counter(suit for _, suit in drawn)

    with open(output_file, "w") as f:
        f.write("Deck of Cards Simulation\n")
        f.write("========================\n\n")
        f.write(f"Drawn {n} cards:\n")
        for card in drawn:
            f.write(f"  {card[0]} of {card[1]}\n")

        f.write("\nSuit Distribution:\n")
        for suit, count in suit_counts.items():
            f.write(f"  {suit}: {count}\n")

    print(f"✅ Results written to {output_file}")


if __name__ == "__main__":
    simulate_deck("deck_results.txt", n=7)   # change n to draw more or fewer cards
