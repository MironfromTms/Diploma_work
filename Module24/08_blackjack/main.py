import random


class Card:
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['✖', '❤️', '🔶', '♠']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        card_value = self.value + self.suit
        return card_value

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
            for value in list(map(str, range(2, 10 + 1))) + ['J', 'Q', 'K', 'A']:
                for suit in ('✖', '♠', '❤️', '🔶'):
                    card = Card(suit=suit, value=value)
                    self.cards.append(card)

            self.shuffle()
        else:
            self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def take(self):
        card = self.cards[0]
        self.cards.remove(self.cards[0])
        return card


class Player:
    def __init__(self, name):
        self.user_name = name
        self.user_cards = []
        self.score = 0
        self.is_playing = True

    def take(self, deck):
        card = deck.take()
        self.user_cards.append(card)

        if card.value in map(str, range(2, 10 + 1)):
            self.score += int(card.value)
        elif card.value in ('J', 'Q', 'K'):
            self.score += 10
        elif card.value == 'A':
            self.score += 11 if self.score <= 10 else 1

    def stop_playing(self):
        self.is_playing = False


start_the_game = True
cards_desk = Deck()
first_player = Player('Sashulya')
second_player = Player('CPU')

for _ in range(2):
    first_player.take(cards_desk)
    second_player.take(cards_desk)

while first_player.is_playing or second_player.is_playing:
    if first_player.is_playing:
        print(
            f'{first_player.user_name} has {first_player.user_cards} - {first_player.score} scores.'
            f'{second_player.user_name} has {second_player.user_cards} - {second_player.score} scores')
        if first_player.score == 21:
            print('You are winner! You have 21!')
            first_player.stop_playing()

        print('1. Take a card')
        print('2. Stop')
        choice = int(input("Take a choice: "))
        if choice == 1:
            first_player.take(cards_desk)
            print(f'You take {first_player.user_cards[-1]}. Your cards now - {first_player.user_cards}')
            if first_player.score > 21:
                print('CPU winner! You take more that 21!')
                first_player.stop_playing()
                break
            elif first_player.score == 21:
                print('You are winner! You have 21!')
                first_player.stop_playing()
                break
        elif choice == 2:
            first_player.stop_playing()
        else:
            print('Please choose correct number!')

    if second_player.is_playing:
        if random.randint(0, 1) == 1:
            print('CPU took the card')
            second_player.take(cards_desk)
            print(f'CPU has {second_player.user_cards}. It is - {second_player.score}')
            if second_player.score > 21:
                print('You are winner! CPU take more that 21!')
                second_player.stop_playing()
                break
            elif second_player.score == 21:
                print('CPU winner!')
                second_player.stop_playing()

        else:
            print('CPU has passed')
            second_player.stop_playing()

print(f'{first_player.user_name} has {first_player.user_cards} - {first_player.score} scores.'
      f'{second_player.user_name} has {second_player.user_cards} - {second_player.score} scores')
if first_player.score == second_player.score:
    print('It is draw!')
elif first_player.score > second_player.score and first_player.score < 21:
    print('You are winner!')
elif first_player.score > 21 or first_player.score < second_player.score:
    print('CPU winner!')
