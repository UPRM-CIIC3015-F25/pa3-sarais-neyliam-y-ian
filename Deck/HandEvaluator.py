from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    #lst pa guardar la info de cada carta
    suits = list()
    ranks = list()
    for card in hand:
        suits.append(card.suit)
        ranks.append(card.rank.value)

    #dict de cuantas veces aparece cada suit
    suit_count = dict()
    for suit in suits:
        if suit in suit_count:
            suit_count[suit] += 1
        else:
            suit_count[suit] = 1

    #chequea si hay flush
    is_flush = False
    for v in suit_count.values():
        if v >= 5:
            is_flush = True
            break

    #dict de cuantas veces aparece cada rank
    rank_count = dict()
    for rank in ranks:
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1

    #lst de ranks únicos para el straight
    unique_ranks = list()
    for rank in ranks:
        if rank not in unique_ranks:
            unique_ranks.append(rank)
    if 14 in unique_ranks:  #ace puede valer 1
        unique_ranks.append(1)

    #ordeno ranks unicos manualmente
    number = len(unique_ranks)
    for i in range(number):
        for j in range(i+1, number):
            if unique_ranks[i] > unique_ranks[j]:
                x = unique_ranks[i]
                unique_ranks[i] = unique_ranks[j]
                unique_ranks[j] = x

    #chequea si hay straight
    is_straight = False
    number = len(unique_ranks)
    for i in range(number - 4):
        if unique_ranks[i]+1 == unique_ranks[i+1] and unique_ranks[i]+2 == unique_ranks[i+2] and unique_ranks[i]+3 == unique_ranks[i+3] and unique_ranks[i]+4 == unique_ranks[i+4]:
            is_straight = True
            break

    #lst de counts de cada rank
    counts = list()
    for v in rank_count.values():
        counts.append(v)

    #sort los counts de mayor a menor
    number = len(counts)
    for i in range(number):
        for j in range(i+1, number):
            if counts[i] < counts[j]:
                x = counts[i]
                counts[i] = counts[j]
                counts[j] = x

    #decir q es:
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if 3 in counts:
        return "Three of a Kind"
    if counts[0] == 4:
        return "Four of a Kind"
    if is_flush and is_straight:
        return "Straight Flush"
    if 2 in counts and 3 in counts:
        return "Full House"
    #cuando hay dobles
    doble = 0
    for v in counts:
        if v == 2:
            doble += 1
    if doble == 1:
        return "One Pair"
    if doble >= 2:
        return "Two Pair"
    else:
        return "High Card"
