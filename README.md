## Game Overview
This is the Uno card game, simulated with alogorithms and data structures. Hence, the game rules remain the same (though they are still listed below for clarity).

## Rules of the game
The objective is to be the first player to get rid of all your cards. Each card has a color and a label, and there are special black cards with unique abilities.

1. The game is played with a deck of cards. The deck consists of 112 cards, built from four blocks of 26 cards: one block for each green, red, blue, and yellow colors. Each color has two cards of each rank (0-9), two Draw Two cards, two Skip cards,  two Reverse cards, four Crazy Crazy cards and four Crazy Draw Four cards.

2. Each player is dealt 7 cards face down (note: whether cards are face up or down will never be relevant for our set-up; we have added this info for those who know the game). The remaining cards are placed in a Draw Pile (also face down). There is also a Discard Pile where played cards are placed. The top card from the Draw Pile is then placed in the Discard Pile face up, and the game begins!

3. The player with the lowest index in the collection goes first (determined in our set-up as the player with index 0 in the array of players given as input). Play then proceeds in an increasing order of the player's index. Thus, in our set-up, we will start with the player at index 0 and move up to K where K is the number of players - 1.

4. To play a card, a player puts a card on top of the Discard Pile facing up.

5. A player can only play a card if that card is of the same color, or has the same label (number/reverse/skip) as the one at the top of the Discard Pile. Alternatively, a Crazy card, or a Crazy Draw Four card can always be played. In our set-up, the player starts scanning its cards from index 0, until they find a playable card.

6. If a player can play at least one card, they must. If they cannot, they must draw a card from the Draw Pile. If that card can be played, they must play it. Otherwise, they keep the card and the turn moves to the next player.

7. If a player plays a Crazy Crazy card, the player gets to choose the color to continue play.

8. If a player plays a Crazy Draw Four card, the color is changed to a randomly chosen color, and the next player must draw four cards from the Draw Pile and cannot play either of them. The next player must also skip their turn. The turn then moves to the player after the next player.

9. If the Draw Pile is empty, the Discard Pile (except the top card) is shuffled and placed as the new Draw Pile. (Detailed instructions on how to do this are given in Task 4.)

10. A player wins by playing all their cards. Once a player runs out of cards, the game ends immediately and that player is declared the winner. However, if the last play is a Draw Two or Draw Four card, the next player must draw the appropriate number of cards before the game ends.
