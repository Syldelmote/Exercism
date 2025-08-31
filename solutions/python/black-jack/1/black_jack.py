"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.
    """
    try:
        return int(card)
    except ValueError:
        if card == 'A':
            return 1
        else:
            return 10


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value > card_two_value:
        return card_one
    elif card_two_value > card_one_value :
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
    Hint: if we already have an ace in hand, then the value for the upcoming ace would be 1.
    """
    if card_one == 'A' or card_two == 'A'  or (value_of_card(card_one) + value_of_card(card_two)) > 10:  
        return 1
    else :
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    condition_one = condition_two = False
    if value_of_card(card_one) or value_of_card(card_two) == 10 :
        condition_one = True
    if (card_one == 'A' or card_two == 'A' )and (card_one != card_two) :
        condition_two = True  
    if condition_one and condition_two :
        return True
    else : 
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11    
