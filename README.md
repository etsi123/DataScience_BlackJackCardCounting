# Blackjack Card Counting

In 2019, I saw the movie 21 and immediately took an interest in beating blackjack with card counting. With a little bit of study I quickly learned that, like most things, card counting is quite simple with practice, discpline, and patience. The basic premise is that cards dealt are not replaced into the deck immediately which means that it's possible to predict the cards to come with greater accuracy (If you're familiar with Bayes' theorum, this is a classic example of that). Since Aces and 10-valued cards (Ten, Jack, Queen, King) favor the player and smaller cards (2-6) favor the dealer, we can keep track of the ratio of favorable cards to unfavorable cards that have been dealt. If there is a surplus of favorable cards still to come, players are statistically more likely to be dealt these cards and should raise their initial bets. I wrote this code because it is one thing to be told that this is worth risking money for and another thing to prove that it is.

**Disclaimer:** The writer of this code does not assume any financial responsibility for those who risk their money counting cards with blackjack. There is inherent risk to gambling even with an advantage (Fig. 1). The edge over the casino is very small, very infrequent, and the predicted standard deviation is very large so I recommend only playing with money that one can afford to lose. I further recommend looking into how to calculate risk of ruin, which is the probability of counting cards perfectly but still losing all of the money that the player allocated for this venture. 

Note: It is a common misconception that counting cards is illegal. It is perfectly legal to count cards in BlackJack in all 50 states; how can it be illegal to allow players to use their brains during a game? 

# To run the code : 

    python simulate_blackjack.py num_decks=6 deck_penetration=0.1 num_shoes=20000
    

The number of decks is casino/table dependent but it is in your best interest to seek blackjack games with fewer decks and smaller deck penetration (Fig. 2). More accurate results will be obtained by increasing the number of shoes run. 

Note this code assumes the following set of blackjack rules (rules that I have personally encountered). 

1. Dealer stays on Soft 17. 
2. Splitting is not allowed.
3. Late Surrender is allowed. 
4. Doubling down is permitted for any hand. 
5. Blackjack pays at a 3:2 x initial wager rate (Note : avoid games where blackjack pays 6:5 x initial wager rate, which is also quite common).

# Common Blackjack terms: 

**Blackjack Shoe:** Container that holds multiple standard 52-card decks shuffled together. The shoe allows for more games to be played by reducing shuffle frequency. 

**Bust:** Being dealt a card that causes the player or dealer to exceed 21 and lose instantly. 

**Doubling down:** After the cards have been dealt and it's the players turn to act, a player is allowed to raise their bet by a maximum of 2x the original bet but can only receive one card. This makes doubling down on hands that cannot bust popular. 

**Split:** If two cards have the same-value, many casinos allow players to split the cards into two seperate hands that can be played independently (provided that the player can provide a second-bet equal to the first). Several of the casino's that I have visited did not allow splits. 

**Soft vs hard hand:** An ace can be valued as 1 or an 11. A soft hand is one in which the ace still has the option to be valued as an 11. For example, Ace-6 is referred to as a "soft 17" or "S17" but Ace-6-ten is a "hard 17" or "H17".

**Late Surrender:** The player can surrender his/her bet for half of the initial wager provided that the dealer does not have a blackjack. 

# Common card counting terms: 

**Running count:** The summation of the sequence of cards updated as they are dealt out of the shoe. The counting system used in this code is the high-low system where 2-6 are valued at +1, 7-9 are valued at 0, and 10-Ace are valued at -1. 

**True count:** The running count divided by the number of decks remaining. Larger true counts raise the player's edge over the casino and should be accompanied by raising the bet size. 

**Deck penetration:** Primarily to prevent effective card counting, some fraction of cards in the shoe are not dealt. The greater the number of cards not dealt, the less effective card counting will be. A large deck penetration increases shuffletime so the casino must balance their desire to prevent effective card counters with their desire to play as many hands as possible. 

**Risk of ruin:** The probability of counting cards perfectly but still losing the entire sum of money allocated to this venture. It is a function of player ability (perfect blackjack strategy, card counting, true count conversion), casino rules (number of decks, deck penetration, blackjack payout rate, split rules, doubling after splitting, minimum bet size, etc.). The player's bet spread should be constructed such that the risk of ruin falls within a comfortable range. 

![Money_earned_with_sd](https://user-images.githubusercontent.com/37279371/172241945-bb9ba702-20da-4299-bef3-cd24e59de0f0.png)

Fig. 1 Predicted hourly rate assuming perfect card counting +/- 1 standard deviation. An example of a particularly poor trajectory as a result of negative variance is shown as well. Note that the person's winnings dips well below $0 during the first 200 hours: this is completely possible and likely for some percentage of card counters. Expected value per hour calculated assuming 3 shoes / hour. 

![Deck_pen](https://user-images.githubusercontent.com/37279371/172288068-557a7c44-f2f1-4def-b803-129fe338eded.png)

Fig. 2 The effect of deck penetration on expected value. Deck penetration directly impacts card counting accuracy so this strong dependence is expected. Players should avoid games with poor deck penetration (larger fraction of the deck unplayed). These plots assume the completion of 3 shoes / hour. 





