# Blackjack Card Counting


In 2019, I saw the movie 21 and took an interest in card counting in blackjack. As it turns out, it is really quite simple as long as you practice and follow the rules. The basic premise is that cards dealt are not replaced into the deck immediately which means that it's possible to predict cards to come based upon which have left the deck. Since Aces and large cards (Ten, Jack, Queen, King) favor the player and smaller cards (2-6) favor the dealer, we can keep track of the ratio of favorable cards to unfavorable cards that have been dealt. If there is a surplus of favorable cards yet to be dealt, they are statistically more likely to be dealt to the player and the player should raise his/her bet. 

I wrote this code because it is one thing to be told that this is worth risking money for and another thing to prove that it is. 

# To run the code : 

    python simulate_blackjack.py num_decks=6 deck_penetration=0.1 num_shoes=1000
    

More accurate results will be obtained by increasing the number of shoes run. The number of decks is casino/table dependent but it is in your best interest to seek blackjack games with fewer decks and smaller deck penetration. Some simulations are shown below illustrating these points. 

Note this code assumes the following set of blackjack rules (rules that I have personally encountered). 

1. Dealer stays on Soft 17. 
2. Splitting is not allowed.
3. Late Surrender is allowed. 
4. Doubling down is permitted for any hand. 
5. Blackjack pays at a 3:2*initial wager rate (avoid games where blackjack pays 6:5*initial wager rate, which is also quite common).

# Common Blackjack terms: 

Blackjack Shoe: Container that holds multiple standard 52-card decks shuffled together. The shoe allows for more games to be played by reducing the time between shuffling. 

Doubling down: After the cards have been dealt and it's the players turn to act, a player is allowed to raise their bet by a maximum of 2x the original bet with the restriction that the player will only receive one card. 

Split: If two cards have the same-value, many casinos allow players to split the cards into two seperate hands that can be played independently (provided that the player can provide a second-bet equal to the first). One of the casino's that I visited frequently did not allow splits (likely because of the myth that is necessary to count cards). 

# Common card counting terms: 

Cards dealt WITHOUT replacement: Cards are dealt and not immediately replaced/reshuffled into the deck, allowing for card counting to be possible. 

Running count: The summation of sequence of cards updated as they are dealt out of the shoe. The counting system used in this code is the high-low system where 2-6 are valued at +1, 7-9 are valued at 0, and 10-Ace are valued at -1. 

True count: The running count divided by the number of decks remaining. Larger true counts raise the player's edge over the casino and should be accompanied by raising the bet size. 

Deck penetration: In order to prevent card counting and running out of cards in the middle of a round, some fraction of cards are not dealt. The greater the number of cards not dealt, the less effective card counting will be. 

Risk of ruin: The probability of playing perfect blackjack and counting cards perfectly but still losing the entire sum of money allocated to this venture. It is a function of player ability (perfect blackjack strategy, card counting, true count conversion), casino rules (number of decks, deck penetration, blackjack payout rate, split rules, doubling after splitting, etc.) and should be calculated by the player after winning/losing money. 


## Disclaimer: The writer of this code does not assume any financial responsibility for those who risk their money counting cards with blackjack. Like all ventures that require money to make money, there is an inherent risk to gambling even with an advantage. The edge over the casino is very small, for limited moments throughout a blackjack game, and the predicted standard deviation is large so I recommend only playing with mooney that one can afford to lose. I further recommend looking into a concept known as risk of ruin, which is the probability of counting cards perfectly but still losing all of the money that the player allocated to this venture. With a more conservative bet-spread it's possible to reduce this probability at the loss of some potential reward. 


