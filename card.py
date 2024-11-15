from enum import auto, IntEnum

class CardColor(IntEnum):
    """
    Enum class for the color of the card
    """
    RED = 0
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    CRAZY = auto()


class CardLabel(IntEnum):
    """
    Enum class for the value of the card
    """
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    CRAZY = auto()
    DRAW_FOUR = auto()


class Card:
    def __init__(self, color: CardColor, label: CardLabel) -> None:
        """
        Constructor for the Card class

        Args:
            color (CardColor): The color of the card
            label (CardLabel): The label of the card

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.color = color
        self.label = label

    def __lt__(self, other: 'Card') -> bool:
        """
        Less than comparison for Card objects based on color and label.

        Args:
            other (Card): The other card to compare with

        Returns:
            bool: True if self is less than other, False otherwise

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        if self.color != other.color:
            return self.color < other.color
        else:
            return self.label < other.label

    def __eq__(self, other: object) -> bool:
        """
        Equality comparison for Card objects based on color and label.

        Args:
            other (object): The other object to compare with

        Returns:
            bool: True if self is equal to other, False otherwise

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        if not isinstance(other, Card):
            return False
        return self.color == other.color and self.label == other.label

    def __str__(self) -> str:
        """
        String representation of the Card object.

        Returns:
            str: The string representation of the card

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return f'({self.color.name} {self.label.name})'

    def __repr__(self) -> str:
        """
        Official string representation of the Card object.

        Returns:
            str: The string representation of the card

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return self.__str__()
