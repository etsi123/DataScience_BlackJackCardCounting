# Blackjack Card Counting


In 2019, I saw the movie 21 and took an interest in counting cards in blackjack. Like most things, it is quite simple with practice and discpline. The basic premise behind card counting is that cards dealt are not replaced into the deck immediately which means that it's possible to predict cards to come with greater accuracy. Since Aces and 10-valued cards (Ten, Jack, Queen, King) favor the player and smaller cards (2-6) favor the dealer, we can keep track of the ratio of favorable cards to unfavorable cards that have been dealt. If there is a surplus of favorable cards still to come, players are statistically more likely to be dealt these favorable cards and should raise their initial bets. 

I wrote this code because it is one thing to be told that this is worth risking money for and another thing to prove that it is.

**Disclaimer:** The writer of this code does not assume any financial responsibility for those who risk their money counting cards with blackjack. There is inherent risk to gambling even with an advantage. The edge over the casino is very small, very infrequent, and the predicted standard deviation is very large so I recommend only playing with money that one can afford to lose. I further recommend looking into how to calculate risk of ruin, which is the probability of counting cards perfectly but still losing all of the money that the player allocated to this venture. 

# To run the code : 

    python simulate_blackjack.py num_decks=6 deck_penetration=0.1 num_shoes=20000
    

The number of decks is casino/table dependent but it is in your best interest to seek blackjack games with fewer decks and smaller deck penetration. Some simulations are shown below illustrating these points. More accurate results will be obtained by increasing the number of shoes run. 

Note this code assumes the following set of blackjack rules (rules that I have personally encountered). 

1. Dealer stays on Soft 17. 
2. Splitting is not allowed.
3. Late Surrender is allowed. 
4. Doubling down is permitted for any hand. 
5. Blackjack pays at a 3:2 x initial wager rate (Note : avoid games where blackjack pays 6:5 x initial wager rate, which is also quite common).

# Common Blackjack terms: 

**Blackjack Shoe:** Container that holds multiple standard 52-card decks shuffled together. The shoe allows for more games to be played by reducing the time between shuffling. 

**Doubling down:** After the cards have been dealt and it's the players turn to act, a player is allowed to raise their bet by a maximum of 2x the original bet but can only receive one card. This makes doubling down on hands that cannot bust (exceed 21) quite popular. 

**Split:** If two cards have the same-value, many casinos allow players to split the cards into two seperate hands that can be played independently (provided that the player can provide a second-bet equal to the first). One of the casino's that I visited frequently did not allow splits (likely because of the myth that is necessary to count cards). 

**Soft vs hard hand:** An ace can be valued as 1 or an 11. A soft hand is one in which the ace still has the option to be valued with an 11. For example, Ace-6 is referred to as a "soft 17" or "S17" but Ace-6-ten is a "hard 17" or "H17".

# Common card counting terms: 

**Running count:** The summation of sequence of cards updated as they are dealt out of the shoe. The counting system used in this code is the high-low system where 2-6 are valued at +1, 7-9 are valued at 0, and 10-Ace are valued at -1. 

**True count:** The running count divided by the number of decks remaining. Larger true counts raise the player's edge over the casino and should be accompanied by raising the bet size. 

**Deck penetration:** Primarily to prevent effective card counting, some fraction of cards are not dealt. The greater the number of cards not dealt, the less effective card counting will be. A large deck penetration increases shuffletime so the casino must balance their desire to prevent effective card counters with their desire to play as many hands as possible. 

**Risk of ruin:** The probability of counting cards perfectly but still losing the entire sum of money allocated to this venture. It is a function of player ability (perfect blackjack strategy, card counting, true count conversion), casino rules (number of decks, deck penetration, blackjack payout rate, split rules, doubling after splitting, minimum bet size, etc.) and should be calculated based upon the player's personal risk tolerance. 





