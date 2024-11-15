from data_structures.referential_array import ArrayR
from data_structures.stack_adt import ArrayStack
from constants import Constants
from card import CardColor, CardLabel, Card
from player import Player
from random_gen import RandomGen

class Game:
    """
    Game class to play the game
    """
    def __init__(self) -> None:
        """
        Constructor for the Game class

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.players: ArrayR[Player] = None
        self.draw_pile: ArrayStack[Card] = ArrayStack(Constants.DECK_SIZE)
        self.discard_pile: ArrayStack[Card] = ArrayStack(Constants.DECK_SIZE)
        self.current_player: Player = None
        self.current_color: CardColor = None
        self.current_label: CardLabel = None

    def generate_cards(self) -> ArrayR[Card]:
        """
        Method to generate the cards for the game

        Returns:
            ArrayR[Card]: The array of Card objects generated

        Complexity:
            O(N) where N is Constants.DECK_SIZE
        """
        list_of_cards: ArrayR[Card] = ArrayR(Constants.DECK_SIZE)
        idx = 0

        # For each color except CRAZY
        for color in CardColor:
            if color != CardColor.CRAZY:
                # Add one ZERO card
                list_of_cards[idx] = Card(color, CardLabel.ZERO)
                idx += 1

                # Add two of each from ONE to NINE
                for num in range(1, 10):  # Numbers from 1 to 9
                    for _ in range(2):
                        list_of_cards[idx] = Card(color, CardLabel(num))
                        idx += 1

                # Add two of each special card: SKIP, REVERSE, DRAW_TWO
                for _ in range(2):
                    list_of_cards[idx] = Card(color, CardLabel.SKIP)
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel.REVERSE)
                    idx += 1
                    list_of_cards[idx] = Card(color, CardLabel.DRAW_TWO)
                    idx += 1
        # Add CRAZY cards
        for _ in range(4):
            list_of_cards[idx] = Card(CardColor.CRAZY, CardLabel.CRAZY)
            idx += 1
            list_of_cards[idx] = Card(CardColor.CRAZY, CardLabel.DRAW_FOUR)
            idx += 1

        # Verify the deck size
        if idx != Constants.DECK_SIZE:
            raise ValueError(f"Generated {idx} cards, expected {Constants.DECK_SIZE}")

        # Shuffle the cards
        RandomGen.random_shuffle(list_of_cards)

        return list_of_cards

    def initialise_game(self, players: ArrayR[Player]) -> None:
        """
        Method to initialise the game

        Args:
            players (ArrayR[Player]): The array of players

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)
            Where N is the total number of cards
        """
        self.players = players

        # Generate the cards
        deck = self.generate_cards()

        num_players = len(players)
        num_cards_per_player = Constants.NUM_CARDS_AT_INIT
        total_cards = Constants.DECK_SIZE

        # Deal cards to players
        # Starting from card index 0 and player index 0
        card_index = 0

        for _ in range(num_cards_per_player):
            for player_index in range(num_players):
                # Give deck[card_index] to players[player_index]
                players[player_index].add_card(deck[card_index])
                card_index += 1

        # From where we left off, add remaining cards to draw_pile
        # Ensuring the last index of the generated cards ends up at the top of the draw_pile
        for idx in range(card_index, total_cards):
            self.draw_pile.push(deck[idx])

        # Now draw a card to be the top of the discard_pile
        # The card should be a number card (0-9)
        while True:
            if self.draw_pile.is_empty():
                # Should not happen during initialisation
                raise Exception("Draw pile is empty during initialisation")
            card = self.draw_pile.pop()
            self.discard_pile.push(card)
            if CardLabel.ZERO.value <= card.label.value <= CardLabel.NINE.value:
                # It's a number card
                self.current_color = card.color
                self.current_label = card.label
                break
            else:
                # Special card, continue drawing
                continue
