from card import Card
from data_structures.array_sorted_list import ArraySortedList
from constants import Constants

class Player:
    """
    Player class to store the player details
    """
    def __init__(self, name: str, position: int) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.name = name
        self.position = position
        self.hand = ArraySortedList[Card](Constants.DECK_SIZE)

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity: O(log N)
            Worst Case Complexity: O(N), due to shifting elements during insertion
            where N is the number of cards in the hand
        """
        self.hand.add(card)

    def play_card(self, index: int) -> Card:
        """
        Method to play a card from the player's hand

        Args:
            index (int): The index of the card to be played

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(N), due to shifting elements during deletion
            where N is the number of cards in the hand
        """
        if index < 0 or index >= len(self.hand):
            raise IndexError("Index out of range")
        card = self.hand.delete_at_index(index)
        return card

    def __len__(self) -> int:
        """
        Method to get the number of cards in the player's hand

        Returns:
            int: The number of cards in the player's hand

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return len(self.hand)

    def __getitem__(self, index: int) -> Card:
        """
        Method to get the card at the given index from the player's hand

        Args:
            index (int): The index of the card to be fetched

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        if index < 0 or index >= len(self.hand):
            raise IndexError("Index out of range")
        return self.hand[index]

    def __str__(self) -> str:
        """
        String representation of the Player object.

        Returns:
            str: The string representation of the player

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N), where N is the number of cards in the hand
        """
        hand_str = ', '.join(str(card) for card in self.hand)
        return f'Player {self.name} (Position {self.position}): [{hand_str}]'

    def __repr__(self) -> str:
        """
        Official string representation of the Player object.

        Returns:
            str: The string representation of the player

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N), where N is the number of cards in the hand
        """
        return self.__str__()
