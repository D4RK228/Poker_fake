from random import random
from check import winner

def new_hand(k_player):
    data_cards = []

    for i in range(k_player * 2 + 5):

        f = False

        while f == False:

            n = int(random() * 51 + 1)

            f = True

            for i in range(len(data_cards)):

                if data_cards[i] == n:
                    f = False

        data_cards.append(n)

    return data_cards



def after_reaver(data_pots, data_cards, data_chips, k_player):
    k_pots = 1

    for i in range(2, k_player + 1):

        if data_pots[i][0] == 0:
            break

        k_pots += 1

    for i in range(1, k_pots + 1):

        max = 0

        print(i)

        for j in range(1, k_player + 1):

            if (data_pots[i][j] == 1):

                if winner(j, data_cards, k_player) > max:
                    max = winner(j, data_cards, k_player)

        kol = 0

        for j in range(1, k_player + 1):

            if (data_pots[i][j] == 1):

                if winner(j, data_cards, k_player) == max:
                    kol += 1

        for j in range(1, k_player + 1):

            if (data_pots[i][j] == 1):

                if winner(j, data_cards, k_player) == max:
                    data_chips[j] += int(data_pots[i][0] / kol)

    return data_chips


def exchange(data_pots, data_bets, data_ingame, k):
    for i in range(1, k + 1):
        data_pots[0][i] = data_ingame[i]

    k_pots = 1

    f = False

    s_iz_2 = -1

    mx = -1

    for i in range(1, k + 1):

        if data_ingame[i] == 2 and data_bets[i] > s_iz_2:
            s_iz_2 = data_bets[i]

        if data_bets[i] > mx:
            mx = data_bets[i]

    if mx == s_iz_2 and mx != 0:
        f = True

    while data_pots[k_pots + 1][0] != 0:
        k_pots += 1

    if data_pots[k_pots][0] == -1 and data_bets.count(0) < k + 1:
        data_pots[k_pots][0] = 0

    if mx != 0:

        for i in range(1, k + 1):

            if data_ingame[i] == 2 and data_bets[i] == 0:
                data_ingame[i] = 0

    while data_bets.count(0) < k + 1:

        pot = 0

        temp = []

        for i in range(1, k + 1):

            if data_ingame[i] > 0:
                data_pots[k_pots][i] = 1

                temp.append(data_bets[i])

        mn = -1

        for i in temp:

            if i < mn or mn == -1:
                mn = i

        for i in range(1, k + 1):

            if data_ingame[i] > 0:

                if data_bets[i] > mn:

                    data_bets[i] -= mn

                    pot += mn

                else:

                    data_bets[i] = 0

                    pot += mn

                    data_ingame[i] = 0

            if data_ingame[i] == 0:

                if data_bets[i] > mn:

                    data_bets[i] -= mn

                    pot += mn

                else:

                    pot += data_bets[i]

                    data_bets[i] = 0

        data_pots[k_pots][0] = data_pots[k_pots][0] + pot

        k_pots += 1

    if f == True:
        data_pots[k_pots][0] = -1

    return data_pots


def after_exchange(data_pots, data_bet, data_ingame, k):
    for i in range(1, k + 1):

        if data_pots[0][i] == 0:

            for j in range(1, k + 1):
                data_pots[j][i] = 0

    return data_pots


def win_prob_flop(k, data_cards, data_ingame):
    data_probs = [0] * k

    s = 0

    p = 0

    data_cards1 = data_cards[:len(data_cards) - 2]

    data_cards1.append(-1)

    data_cards1.append(-1)

    for i in range(1, 53):

        if i not in data_cards1:

            for j in range(1, 53):

                if j not in data_cards1 and j != i:

                    p += 1

                    data_cards1[k * 2 + 3] = i

                    data_cards1[k * 2 + 4] = j

                    for l in range(k):

                        if data_ingame[l + 1] != 0:
                            data_probs[l] = winner(l + 1, data_cards1, k)

                    if max(data_probs) == data_probs[0]:
                        s += 1

                    data_cards1[k * 2 + 4] = -1

                    data_cards1[k * 2 + 3] = -1

    x = (s / p)

    return x


def win_prob_turn(k, data_cards, data_ingame):
    data_probs = [0] * k

    s = 0

    p = 0

    data_cards1 = data_cards[:len(data_cards) - 1]

    data_cards1.append(-1)

    for j in range(1, 53):

        if j not in data_cards1:

            p += 1

            data_cards1[k * 2 + 4] = j

            for l in range(k):

                if data_ingame[l + 1] != 0:
                    data_probs[l] = winner(l + 1, data_cards1, k)

            if max(data_probs) == data_probs[0]:
                s += 1

            data_cards1[k * 2 + 4] = -1

    x = (s / p)

    return x
