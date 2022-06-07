#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#author: evantsiklidis


import sys
from random import shuffle
import matplotlib.pyplot as plt
import pandas as pd
import collections
import random




card_dict = { "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10,"Ace":11}
counting_rules = { "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1,"Ace":-1}
decision_chart = pd.read_csv('blackjackstratchart_s17.csv')




def create_shoe(num_decks):
    """
    Parameters
    ----------
    num_decks : The Number of decks used to construct the shoe that will be played with. 
    This is chosen by the casino and fewer decks favors the player. 
    Returns
    -------
    shoe : The shuffled shoe. num_decks combined into one massive deck and shuffled. 

    """
    shoe = []
    for i in range(num_decks):
        for j in range(0,4): 
            unique_cards = list(card_dict.keys())
            shoe = shoe + unique_cards
    shuffle(shoe)
    return shoe

def deal_round(): 
    """
    Returns
    -------
    Deal out the cards to the players and, importantly, remove them from the shoe without replacement. 

    """
    playercard1 = curr_shoe.pop(0)
    playercard2 = curr_shoe.pop(0)
    dealercard1 = curr_shoe.pop(0)
    dealercard2 = curr_shoe.pop(0)
    return [playercard1,playercard2],[dealercard1,dealercard2]

def my_bet(min_bet,true_count):
    """
    

    Parameters
    ----------
    min_bet : The minimum bet placed per hand, usually established by the casino but really 
    represents a minimum basis point. 
    true_count : The true-count is used to determine our bet. 

    Returns
    -------
    bet : What is the bet. 

    """
    if true_count >= 6: 
        bet = min_bet*20
    elif true_count >= 5 and true_count < 6: 
        bet = min_bet*15
    elif true_count >= 4 and true_count < 5: 
        bet = min_bet*10
    elif true_count >=3 and true_count < 4: 
        bet = min_bet*5
    elif true_count >= 2 and true_count < 3:
        bet = min_bet * 3
    elif true_count >= 1 and true_count < 2: 
        bet = min_bet*2
    else: 
        bet = 0
    return bet

def hit(): 
    """
    Returns
    -------
    Returns the next card and removes it from the shoe. 

    """
    return curr_shoe.pop(0)

def check_for_blackjack(playercards,dealercards): 
    """
    Parameters
    ----------
    playercards : The cards dealt to the plater. 
    dealercards : The cards dealt to  the dealer. 

    Returns
    -------
    int Returns 2 flags, the first indicating if a player has a blackjack and therefore the hand is done and the next indicating if it is a winner, loser, push, or play on. 

    """
    if ("Ace" in playercards) and ("Ten" in playercards or "Jack" in playercards or "Queen" in playercards or "King" in playercards): 
        player_bj = 1
    else: 
        player_bj = 0
    if ("Ace" in dealercards) and ("Ten" in dealercards or "Jack" in dealercards or "Queen" in dealercards or "King" in dealercards): 
        dealer_bj = 1
    else: 
        dealer_bj = 0
    if player_bj == 1 and dealer_bj == 0: 
        return 1,1 
    elif player_bj == 0 and dealer_bj == 0: 
        return 0,0
    elif player_bj == 1 and dealer_bj == 1: 
        return 1,0
    elif player_bj == 0 and dealer_bj == 1: 
        return 1,-1

def get_action(playercards,dealerupcard): 
    """
    Parameters
    ----------
    playercards : What are the player cards, which card is visible for the dealer. These three pieces of information can be used to determine the optimal action. 
    Returns
    -------
    action : Returns the decision to either hit, surrender, double, or stay. Note, splitting is not allowed at this casino. 

    """
    label = check_hand_value(playercards)
    action = decision_chart[decision_chart['Player'] == label][dealerupcard].iloc[0]
    return action
        
def check_hand_value(input_cards): 
    """
    Parameters
    ----------
    input_cards : Given the cards, determine what the value is (e.g., S17 : Soft 17 --> Ace currently counts as 11 but could also count as 1. 
    H17 vs a 2 is a stay but S17 vs a 2 is a hit. So important to compute Hard vs Soft hands. )

    Returns
    -------
    label : Returnt the official handvalue (e.g., S17)

    """
    hand_value = 0
    for card in input_cards:
        hand_value = hand_value + card_dict[card]
    if "Ace" not in input_cards: 
        label = "H" + str(hand_value)
    if "Ace" in input_cards and hand_value < 21.5: 
        label = "S"+str(hand_value)
    if "Ace" in input_cards and hand_value > 21:
        num_aces = collections.Counter(input_cards)['Ace']
        counter = 0
        while hand_value > 21 and counter < num_aces: 
            hand_value = hand_value - 10
            counter = counter + 1
            if hand_value> 10 and hand_value < 21 and counter < num_aces:
                label = "S"+str(hand_value)
                break
            else: 
                label = "H"+str(hand_value)
    return label

def update_running_count(running_count,roundcards): 
    """
    Parameters
    ----------
    running_count : Now that we have seen new cards, let's update the running count based upon the value assigned in the counting_rules dictionary. 
    This is consistent with the high-low counting method where low cards (2-6) are given a value of +1 and large cards (10-Ace) are given a value of -1. Middle cards
    (7-9) are assigned a value of 0. 
    roundcards : The cards seen in the round of hands just dealt. Every single card should be accounted for to make this method work most accurately.

    Returns
    -------
    running_count : Updated running count returned. 

    """
    for card in roundcards: 
        running_count += counting_rules[card]
    return running_count
        
def update_tc(curr_shoe,running_count): 
    """
    Parameters
    ----------
    curr_shoe : Update the true count based upon the number of cards remaining in the deck and the running count. 

    Returns
    -------
    Returns the true count which is used to determine the bet spread. 

    """
    num_decks_remaining = len(curr_shoe) / 52
    return running_count / num_decks_remaining

def payout(bj,win_flag,round_winning,bet): 
    """
    Parameters
    ----------
    bj : Was there a blackjack? If so, we get paid at a rate of 1.5x our bet and if we lose, we only lose our bet. This is important because this advantage 
    is entirely how card counting is possible. Many casinos offer games that pay blackjacks at a rate of 1.2x our bet, which is almost impossibvle to beat with card counting. 
    win_flag : Did we win or lose
    round_winning : Update the winning tracker. 
    bet : Use bet information. 

    Returns
    -------
    round_winning : Updated winnings tracker. 

    """
    if bj == 1: 
        round_winning += 1.5*bet         
        return round_winning
    if bj == -1 or win_flag == 0: 
        round_winning -= bet         
        return round_winning
    if bj == 0 and win_flag == 1: 
        round_winning += bet         
        return round_winning     
    return round_winning

def plot_ev_chart(mean_hour=27, sd_hour = 311): 
    """

    Parameters
    ----------
    mean_hour : Mean hourly payout. Calculated after simulations are run. 
    sd_hour : Standard deviation of the hourly payout. Calculated after simulations are run. 

    Returns
    -------
    Creates a figure. 

    """
    num_hours=1000
    xdata = [0]
    hour_list = [0]
    upper_list = [0]
    lower_list = [0]
    cum_sum = 0
    example = [0]
    for i in range(1,num_hours):
        xdata.append(i)
        ev = i*mean_hour
        hour_list.append(ev)
        upper_list.append(ev + (sd_hour *sd_hour* i)**(0.5))
        lower_list.append(ev - (sd_hour *sd_hour* i)**(0.5))
        cum_sum = cum_sum + random.normalvariate(mean_hour, sd_hour)
        example.append(cum_sum)
        
    label = 'Expected Value = $' + str(mean_hour) + '/hour'
    plt.plot(xdata, hour_list, 'or',label=label)
    plt.plot(xdata, example,label='Example Card Counter')

    plt.fill_between(xdata, lower_list, upper_list,
                 color='gray', alpha=0.2,label = '+/- 1 SD')
    
    plt.ylabel('Total Money Earned')
    plt.xlabel('Hours Played')
    plt.title('Money Earned vs Hours Played')
    plt.legend(loc = 'upper left')
    plt.show()

def plot_deckpen_impact(mean_hourly_rates=[27,19,9,7,3],pens=[0.1,0.2,0.3,0.4,0.5]): 
    """
    Parameters
    ----------
    mean_hourly_rates : Expected hourly rate values as a function of deck penetration. 
    Pens: deck penetration values

    Returns
    -------
    Creates a figure. 
    """
    num_hours = 1000
    xdata = [0]
    ev_list = []
    label_list = ['Deck Pen = 0.1','Deck Pen = 0.2','Deck Pen = 0.3','Deck Pen = 0.4', 'Deck Pen = 0.5']
    for i in range(1,num_hours): 
        xdata.append(i)
    
    for mean_hour in mean_hourly_rates: 
        temp = []
        for i in range(0,num_hours): 
            ev = i*mean_hour
            temp.append(ev)
        ev_list.append(temp)


    for i in range(len(mean_hourly_rates)): 
        plt.plot(xdata,ev_list[i],label = label_list[i])
    plt.xlabel('Hours Played')
    plt.ylabel('Total Money Earned')
    plt.title('Money Earned vs Hours Played')
    plt.legend(loc = 'upper left')    
    plt.show()



#Driver code. 
if __name__ == "__main__":

    num_decks,deck_penetration,min_bet,num_shoes = int(sys.argv[1].split('=')[1]),float(sys.argv[2].split('=')[1])\
    ,int(sys.argv[3].split('=')[1]),int(sys.argv[4].split('=')[1])

    print('********************************************************')
    print('Number of decks is ' + str(num_decks))
    print('Penetration is ' + str(deck_penetration))
    print('Minimum bet is ' + str(min_bet))
    print('Number of shoes being run is ' + str(num_shoes))
    print('********************************************************')

    round_winning_tracker = [] #Keep track of the winnings of each shoe (could be positive or negative)
    for shoe_number in range(num_shoes):
        print("Dealing shoe number : " + str(shoe_number)) #Keep track of code progress
        curr_shoe = create_shoe(num_decks) #Construct the current shoe.
        total_num_cards = len(curr_shoe) #How many cards are there? (Should just be 52 * number of decks)
        deal_card = int(len(curr_shoe)*deck_penetration) #The deal_card indicates when it's time to stop playing and shuffle. Casino's don't play until the last card. 
        running_count,true_count,round_winning = 0,0,0 #Initialize every shoe with 0 running count / true count and no winnings yet. 
        roundcards = []# to keep track of the running count after every round. 
        while len(curr_shoe) > deal_card:  #Iterate through every round until we reach the deal card. 
            running_count = update_running_count(running_count,roundcards) #Update the running count based on cards from previous round. 
            roundcards = [] #Start a fresh round of cards
            true_count = update_tc(curr_shoe,running_count) #Calculate the true count based upon the number of decks remaining and number of cards left in the shoe. 
            bet = my_bet(min_bet,true_count) #Update my bet. 
            playercards,dealercards = deal_round() #Deal our the cards. This assumes one player and one dealer but can be rewritten for a variable number of players. 
            #Note, it has been shown that adding more players does not affect your probability of winning hands so long as you update what cards they had as well/ 
            
            #After cards are dealt, did anybody get a blackjack? Blackjack is the first thing to check for every round. 
            hand_finished_flag,bj = check_for_blackjack(playercards,dealercards)
            round_winning = payout(bj,-1,round_winning,bet)
    

            #Is the hand-finished? There is no player actions if the dealer or player had a blackjack. 
            #Player action code. 
            if hand_finished_flag == 0: 
                dealerupcard = dealercards[0]
                decision_time = 1
                while decision_time == 1: 
                    action = get_action(playercards,dealerupcard)
                    if action == "H": 
                        playercards.append(hit())
                        label = check_hand_value(playercards)
                        if label[0] == 'H' and int(label[1:]) > 21: 
                            decision_time = 0
                            hand_finished_flag = 1
                            round_winning = payout(0,0,round_winning,bet)
                    if action == "Sr": 
                        round_winning = round_winning - 0.5*bet
                        hand_finished_flag,decision_time = 1,0
                    if action == "S": 
                        decision_time = 0
                    if action == "D": 
                        decision_time = 0
                        bet = 2*bet
                        playercards.append(hit())
            #Dealer acts after player. If the players haven't all busted and still have live hands, then it's time for the dealer to reveal his second card and 
            #either draw more cards or stand. Note, this assumes dealers stay on S17. This is a common rule in PA, but less common than in other parts of the US. 
            #Perhaps non-intuitely, it is to the players advantage if the dealer does not hit S17. 
            if hand_finished_flag == 0:
                decision_time = 1
                label = check_hand_value(dealercards)
                while decision_time == 1: 
                    if int(label[1:]) <= 16:
                        card = curr_shoe.pop(0)
                        dealercards.append(card)
                    player_value = int(check_hand_value(playercards)[1:])
                    dealer_value = int(check_hand_value(dealercards)[1:])
                    if dealer_value > 16: 
                        decision_time = 0
                hand_finished_flag = 1
                if  player_value>dealer_value or dealer_value > 21: 
                    round_winning = payout(0,1,round_winning,bet)
                if player_value<dealer_value and dealer_value <=21:
                    round_winning = payout(0,0,round_winning,bet)
            #Update card seen this round. 
            if hand_finished_flag == 1: 
                roundcards = roundcards + playercards+dealercards
    
        round_winning_tracker.append(round_winning) 
        total_money_won = sum(round_winning_tracker)
        
    #Summarize what happened. 
    print("Averaged " + str(total_money_won / num_shoes) + " per shoe")
    print("If we assume 3 shoes / hour : $" + str(total_money_won*3 / num_shoes) + ' / hour')                
    mean = sum(round_winning_tracker) / len(round_winning_tracker)
    variance = sum([((x - mean) ** 2) for x in round_winning_tracker]) / len(round_winning_tracker)
    sd = variance ** 0.5
    sd_hour = (3*sd*sd)**(0.5)
    print("Standard deviation per hour is  : $" + str(sd_hour))
    mean_hour = total_money_won*3 / num_shoes
    
    plot_ev_chart()
    plot_deckpen_impact()


            
        
                
            
            
        
        
        
        
        
        
        
            
        
        
    
        
    
    


