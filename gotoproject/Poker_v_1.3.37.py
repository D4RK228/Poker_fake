from random import random
from tkinter import *
from PIL import ImageTk, Image
import time
import threading
import PIL

def player_bet(a):
    global temporary
    global prev_bet
    print('a', a)
    if a == 1:
        temporary = -2
    if a == 2:
        temporary = 0
    if a == 3:
        temporary = 0
    print(temporary)

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


def straight_flash(player, data_cards, k_player):
    data_comb = []  # комбинация игрока

    data_comb_n = []  # номиналы комбинции

    data_comb_m = []  # масти комбинации

    data_comb.append(data_cards[player * 2 - 2])

    data_comb.append(data_cards[player * 2 - 1])

    s = 0

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb_m.append((data_comb[i] - 1) // 13 + 1)

    data_comb_m.sort()

    for i in range(3):

        if data_comb_m[i] == data_comb_m[i + 1] and data_comb_m[i] == data_comb_m[i + 2] and data_comb_m[i] == \
                data_comb_m[i + 3] and data_comb_m[i] == data_comb_m[i + 4]:
            s = data_comb_m[i]

    if s == 0:

        return 0

    else:

        data_comb.sort()

        data_comb_m.sort()

        for i in range(7):

            if data_comb_m[i] == s:

                if data_comb[i] % 13 == 0:
                    data_comb_n.append(13)

                data_comb_n.append(data_comb[i] % 13)

        data_comb_n.sort()

        a = 0

        for i in range(len(data_comb_n) - 4):

            if data_comb_n[i] == data_comb_n[i + 1] - 1 and data_comb_n[i] == data_comb_n[i + 2] - 2 and data_comb_n[
                i] == data_comb_n[i + 3] - 3 and data_comb_n[i] == data_comb_n[i + 4] - 4:
                a = data_comb_n[i + 4]

        return a


def straight(player, data_cards, k_player):
    data_comb = []

    data_comb.append(data_cards[player * 2 - 1])

    data_comb.append(data_cards[player * 2 - 2])

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb[i] = data_comb[i] % 13

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb.append(13)

    data_comb.sort()

    f = True

    while f == True:

        for i in range(len(data_comb) - 1):

            f = False

            if data_comb[i] == data_comb[i + 1]:
                data_comb.pop(i)

                f = True

                break

    s = 0

    if len(data_comb) >= 5:

        for i in range(len(data_comb) - 4):

            if data_comb[i] == data_comb[i + 1] - 1 and data_comb[i] == data_comb[i + 2] - 2 and data_comb[i] == \
                    data_comb[i + 3] - 3 and data_comb[i] == data_comb[i + 4] - 4:
                s = data_comb[i + 4]

    return s


def flash(player, data_cards, k_player):
    data_comb = []  # комбинация игрока

    data_comb_n = []  # номиналы комбинции

    data_comb_m = []  # масти комбинации

    data_comb.append(data_cards[player * 2 - 2])

    data_comb.append(data_cards[player * 2 - 1])

    s = 0

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb_m.append((data_comb[i] - 1) // 13 + 1)

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb[i] = 13

    data_comb_m.sort()

    for i in range(3):

        if data_comb_m[i] == data_comb_m[i + 1] and data_comb_m[i] == data_comb_m[i + 2] and data_comb_m[i] == \
                data_comb_m[i + 3] and data_comb_m[i] == data_comb_m[i + 4]:
            s = data_comb_m[i]

    if s == 0:

        return 0

    else:

        for i in range(7):

            if (data_comb[i] - 1) // 13 + 1 == s:
                data_comb_n.append(data_comb[i] % 13)

        for i in range(len(data_comb_n)):

            if data_comb_n[i] == 0:
                data_comb_n[i] = 13

        data_comb_n.sort()

        return data_comb_n[len(data_comb_n) - 1]


def quards(player, data_cards, k_player):
    data_comb = []

    data_comb.append(data_cards[player * 2 - 1])

    data_comb.append(data_cards[player * 2 - 2])

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb[i] = data_comb[i] % 13

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb[i] = 13

    data_comb.sort()

    s = 0

    for i in range(len(data_comb) - 3):

        if data_comb[i] == data_comb[i + 3]:
            s = data_comb[i]

            data_comb[i] = -1

            data_comb[i + 1] = -1

            data_comb[i + 2] = -1

            data_comb[i + 3] = -1

    if s != 0:

        data_comb.sort()

        data_comb.reverse()

        s *= 100

        s += data_comb[0]

        return s

    else:

        return 0


def full_house(player, data_cards, k_player):
    data_comb = []

    data_comb.append(data_cards[player * 2 - 1])

    data_comb.append(data_cards[player * 2 - 2])

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb[i] = data_comb[i] % 13

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb[i] = 13

    data_comb.sort()

    data_comb.reverse()

    s = 0

    for i in range(5):

        if data_comb[i] == data_comb[i + 2]:
            s = data_comb[i]

            data_comb[i] = -1

            data_comb[i + 1] = -1

            data_comb[i + 2] = -1

            break

    s *= 100

    a = 0

    data_comb.sort()

    data_comb.reverse()

    for i in range(4):

        if data_comb[i] == data_comb[i + 1]:
            a = data_comb[i]

            break

    if a != 0 and s != 0:

        s += a

        return s

    else:

        return 0


def three(player, data_cards, k_player):
    data_comb = []

    data_comb.append(data_cards[player * 2 - 1])

    data_comb.append(data_cards[player * 2 - 2])

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb[i] = data_comb[i] % 13

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb[i] = 13

    data_comb.sort()

    data_comb.reverse()

    s = 0

    for i in range(5):

        if data_comb[i] == data_comb[i + 2]:
            s = data_comb[i]

            data_comb[i] = -1

            data_comb[i + 1] = -1

            data_comb[i + 2] = -1

            break

    if s != 0:

        s *= 100

        data_comb.sort()

        data_comb.reverse()

        s += data_comb[0]

        s *= 100

        data_comb[0] = -1

        data_comb.sort()

        data_comb.reverse()

        s += data_comb[0]

        return s

    else:

        return 0


def two_pairs(player, data_cards, k_player):
    data_comb = []

    data_comb.append(data_cards[player * 2 - 1])

    data_comb.append(data_cards[player * 2 - 2])

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb[i] = data_comb[i] % 13

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb[i] = 13

    data_comb.sort()

    data_comb.reverse()

    s = 0

    for i in range(6):

        if data_comb[i] == data_comb[i + 1]:
            s = data_comb[i]

            data_comb[i] = -1

            data_comb[i + 1] = -1

            break

    data_comb.sort()

    data_comb.reverse()

    a = 0

    for i in range(6):

        if data_comb[i] == data_comb[i + 1] and data_comb[i] != -1:
            a = data_comb[i]

            data_comb[i] = -1

            data_comb[i + 1] = -1

            break

    if a != 0 and s != 0:

        data_comb.sort()

        data_comb.reverse()

        s *= 100

        s += a

        s *= 100

        s += data_comb[0]

        return s

    else:

        return 0


def pair(player, data_cards, k_player):
    data_comb = []

    data_comb.append(data_cards[player * 2 - 1])

    data_comb.append(data_cards[player * 2 - 2])

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb[i] = data_comb[i] % 13

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb[i] = 13

    data_comb.sort()

    data_comb.reverse()

    s = 0

    for i in range(6):

        if data_comb[i] == data_comb[i + 1]:
            s = data_comb[i]

            data_comb[i] = -1

            data_comb[i + 1] = -1

            break

    if s != 0:

        for i in range(3):
            data_comb.sort()

            data_comb.reverse()

            s *= 100

            s += data_comb[0]

            data_comb[0] = -1

        return s

    else:

        return 0


def kicker(player, data_cards, k_player):
    data_comb = []

    data_comb.append(data_cards[player * 2 - 1])

    data_comb.append(data_cards[player * 2 - 2])

    for i in range(5):
        data_comb.append(data_cards[k_player * 2 + i])

    for i in range(7):
        data_comb[i] = data_comb[i] % 13

    for i in range(7):

        if (data_comb[i] == 0):
            data_comb[i] = 13

    s = 0

    data_comb.sort()

    data_comb.reverse()

    s += data_comb[0]

    data_comb[0] = 0

    for i in range(4):
        data_comb.sort()

        data_comb.reverse()

        s *= 100

        s += data_comb[0]

        data_comb[0] = -1

    return s


def winner(player, data_cards, k_player):
    k = player

    if straight_flash(k, data_cards, k_player) != 0:

        return (900000000000 + straight_flash(k, data_cards, k_player))

    elif quards(k, data_cards, k_player) != 0:

        return (800000000000 + quards(k, data_cards, k_player))

    elif full_house(k, data_cards, k_player) != 0:

        return (700000000000 + full_house(k, data_cards, k_player))

    elif flash(k, data_cards, k_player) != 0:

        return (600000000000 + flash(k, data_cards, k_player))

    elif straight(k, data_cards, k_player) != 0:

        return (500000000000 + straight(k, data_cards, k_player))

    elif three(k, data_cards, k_player) != 0:

        return (400000000000 + three(k, data_cards, k_player))

    elif two_pairs(k, data_cards, k_player) != 0:

        return (300000000000 + two_pairs(k, data_cards, k_player))

    elif pair(k, data_cards, k_player) != 0:

        return (200000000000 + pair(k, data_cards, k_player))

    elif kicker(k, data_cards, k_player) != 0:

        return (100000000000 + kicker(k, data_cards, k_player))


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


def bot_preflop(card1, card2, bet, prev_bet, chips,
                last_move):  # bet - разница между последними двумя изменениями ставок

    x = card1 % 13

    y = card2 % 13

    if x == 0:
        x = 13

    if y == 0:
        y = 13

    if x + y >= 22:

        r = random()

        if r > 0.1:

            stavka = int(bet * (random() * 2 + 1)) + prev_bet

        else:

            stavka = prev_bet

        if stavka > chips + last_move:

            return chips + last_move

        else:

            return stavka

    if x + y > 7 or x == y:

        r = random()

        if r < 0.15:

            return 0

        else:

            if r > 0.9:

                stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

    if x + y <= 7:

        r = random()

        if r < 0.6:

            return 0

        else:

            if r > 0.95:

                stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka


def bot_flop(card1, card2, data_flop, bet, prev_bet, chips, last_move):  # если никто не ставил, тогда bet = bigblind

    data_card = []

    data_card.append(card1)

    data_card.append(card2)

    data_card.extend(data_flop)

    f = False

    while f == False:

        f = True

        cardturn = random() * 51 + 1

        if cardturn in data_card:
            f = False

    f = False

    data_card.append(cardturn)

    while f == False:

        f = True

        cardreaver = random() * 51 + 1

        if cardreaver in data_card:
            f = False

    data_card.append(cardreaver)

    if winner(1, data_card, 1) < 200000000000:

        r = random()

        if r < 0.9:

            return 0

        else:

            if r > 0.98:

                stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

    if winner(1, data_card, 1) < 500000000000:

        r = random()

        if r < 0.1:

            return 0

        else:

            if r > 0.7:

                stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

    if winner(1, data_card, 1) >= 500000000000:

        r = random()

        if r > 0.1:

            stavka = int(bet * (random() * 2 + 1)) + prev_bet

        else:

            stavka = prev_bet

        if stavka > chips + last_move:

            return chips + last_move

        else:

            return stavka


def bot_turn(card1, card2, data_turn, bet, prev_bet, chips, last_move):
    data_card = []

    data_card.append(card1)

    data_card.append(card2)

    data_card.extend(data_turn)

    f = False

    while f == False:

        f = True

        cardreaver = random() * 51 + 1

        if cardreaver in data_card:
            f = False

    data_card.append(cardreaver)

    if winner(1, data_card, 1) < 300000000000:

        r = random()

        if r < 0.9:

            return 0

        else:

            if r > 0.98:

                stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

    if winner(1, data_card, 1) < 600000000000:

        r = random()

        if r < 0.03:

            return 0

        else:

            if r > 0.7:

                stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips:

                    return chips + last_move

                else:

                    return stavka

    if winner(1, data_card, 1) >= 600000000000:

        r = random()

        if r > 0.1:

            stavka = int(bet * (random() * 2 + 1)) + prev_bet

        else:

            stavka = prev_bet

        if stavka > chips:

            return chips + last_move

        else:

            return stavka


def bot_reaver(card1, card2, data_reaver, bet, prev_bet, chips, last_move):
    data_card = []

    data_card.append(card1)

    data_card.append(card2)

    data_card.extend(data_reaver)

    if winner(1, data_card, 1) < 400000000000:

        r = random()

        if r < 0.9:

            return 0

        else:

            if r > 0.98:

                stavka = stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

    if winner(1, data_card, 1) < 700000000000:

        r = random()

        if r < 0.1:

            return 0

        else:

            if r > 0.7:

                stavka = stavka = int(bet * (random() * 2 + 1)) + prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

            else:

                stavka = prev_bet

                if stavka > chips + last_move:

                    return chips + last_move

                else:

                    return stavka

    if winner(1, data_card, 1) >= 700000000000:

        r = random()

        if r > 0.1:

            stavka = stavka = int(bet * (random() * 2 + 1)) + prev_bet

        else:

            stavka = prev_bet

        if stavka > chips + last_move:

            return chips + last_move

        else:

            return stavka


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
def chips_cfg(data_chips):
    ch1.configure(text=str(data_chips[2]))
    ch2.configure(text=str(data_chips[3]))
    ch3.configure(text=str(data_chips[4]))
    ch4.configure(text=str(data_chips[5]))
    ch5.configure(text=str(data_chips[6]))
    ch6.configure(text=str(data_chips[7]))
    ch7.configure(text=str(data_chips[8]))
    ch8.configure(text=str(data_chips[9]))
def bets_cfg(data_bets):
    b_b_1.configure(text=str(data_bets[2]))
    b_b_2.configure(text=str(data_bets[3]))
    b_b_3.configure(text=str(data_bets[4]))
    b_b_4.configure(text=str(data_bets[5]))
    b_b_5.configure(text=str(data_bets[6]))
    b_b_6.configure(text=str(data_bets[7]))
    b_b_7.configure(text=str(data_bets[8]))
    b_b_8.configure(text=str(data_bets[9]))

window = Tk()
window.title("PokerFake")
window.geometry('800x500')
window.resizable(width=False, height=False)

table = Canvas(window, width=650, height=340)
table.place(x=100, y=50)
table.create_oval(0, 350, 653, 0, fill='green', outline='green')
card_texture = []
card_texture.append("rubashka.jpg")
for i in range(9):
    a = "card-white-cross-" + str(i + 2) + ".png"
    card_texture.append(a)
a = "card-white-cross-"
card_texture.append(a + "junior.png")
card_texture.append(a + "queen.png")
card_texture.append(a + "king.png")
card_texture.append(a + "ace.png")

for i in range(9):
    a = "card-white-diamond-" + str(i + 2) + ".png"
    card_texture.append(a)
a = "card-white-diamond-"
card_texture.append(a + "junior.png")
card_texture.append(a + "queen.png")
card_texture.append(a + "king.png")
card_texture.append(a + "ace.png")

for i in range(9):
    a = "card-white-heart-" + str(i + 2) + ".png"
    card_texture.append(a)
a = "card-white-heart-"
card_texture.append(a + "junior.png")
card_texture.append(a + "queen.png")
card_texture.append(a + "king.png")
card_texture.append(a + "ace.png")

for i in range(9):
    a = "card-white-spear-" + str(i + 2) + ".png"
    card_texture.append(a)
a = "card-white-spear-"
card_texture.append(a + "junior.png")
card_texture.append(a + "queen.png")
card_texture.append(a + "king.png")
card_texture.append(a + "ace.png")



card_texture_small = []
card_texture_small.append("rubashka-small.jpg")
for i in range(9):
    a = "card-white-cross-" + str(i + 2) + "-small.png"
    card_texture_small.append(a)
a = "card-white-cross-"
card_texture_small.append(a + "junior-small.png")
card_texture_small.append(a + "queen-small.png")
card_texture_small.append(a + "king-small.png")
card_texture_small.append(a + "ace-small.png")

for i in range(9):
    a = "card-white-diamond-" + str(i + 2) + "-small.png"
    card_texture_small.append(a)
a = "card-white-diamond-"
card_texture_small.append(a + "junior-small.png")
card_texture_small.append(a + "queen-small.png")
card_texture_small.append(a + "king-small.png")
card_texture_small.append(a + "ace-small.png")

for i in range(9):
    a = "card-white-heart-" + str(i + 2) + "-small.png"
    card_texture_small.append(a)
a = "card-white-heart-"
card_texture_small.append(a + "junior-small.png")
card_texture_small.append(a + "queen-small.png")
card_texture_small.append(a + "king-small.png")
card_texture_small.append(a + "ace-small.png")

for i in range(9):
    a = "card-white-spear-" + str(i + 2) + "-small.png"
    card_texture_small.append(a)
a = "card-white-spear-"
card_texture_small.append(a + "junior-small.png")
card_texture_small.append(a + "queen-small.png")
card_texture_small.append(a + "king-small.png")
card_texture_small.append(a + "ace-small.png")



t1 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
t1.place(x=190, y=145)

pilImage = Image.open(card_texture[0])
image1 = ImageTk.PhotoImage(pilImage)
imagesprite1 = t1.create_image(42, 53, image=image1)

t2 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
t2.place(x=290, y=145)

pilImage = Image.open(card_texture[0])
image2 = ImageTk.PhotoImage(pilImage)
imagesprite2 = t2.create_image(42, 53, image=image2)

t3 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
t3.place(x=390, y=145)

pilImage = Image.open(card_texture[0])
image3 = ImageTk.PhotoImage(pilImage)
imagesprite3 = t3.create_image(42, 53, image=image3)

t4 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
t4.place(x=490, y=145)

pilImage = Image.open(card_texture[0])
image4 = ImageTk.PhotoImage(pilImage)
imagesprite4 = t4.create_image(42, 53, image=image4)

t5 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
t5.place(x=590, y=145)

pilImage = Image.open(card_texture[0])
image5 = ImageTk.PhotoImage(pilImage)
imagesprite5 = t5.create_image(42, 53, image=image5)

p1 = Canvas(window, width=80, height=60, bg="black")
p1.place(x=80, y=270)

p1.create_text(40, 15, text="BOT 1", font=("Arial Bold", 14), fill="red")

p2 = Canvas(window, width=80, height=60, bg="black")
p2.place(x=60, y=100)

p2.create_text(40, 15, text="BOT 2", font=("Arial Bold", 14), fill="red")

p3 = Canvas(window, width=80, height=60, bg="black")
p3.place(x=180, y=5)

p3.create_text(40, 15, text="BOT 3", font=("Arial Bold", 14), fill="red")

p4 = Canvas(window, width=80, height=60, bg="black")
p4.place(x=300, y=5)

p4.create_text(40, 15, text="BOT 4", font=("Arial Bold", 14), fill="red")

p5 = Canvas(window, width=80, height=60, bg="black")
p5.place(x=440, y=5)

p5.create_text(40, 15, text="BOT 5", font=("Arial Bold", 14), fill="red")

p6 = Canvas(window, width=80, height=60, bg="black")
p6.place(x=560, y=5)

p6.create_text(40, 15, text="BOT 6", font=("Arial Bold", 14), fill="red")

p7 = Canvas(window, width=80, height=60, bg="black")
p7.place(x=680, y=70)

p7.create_text(40, 15, text="BOT 7", font=("Arial Bold", 14), fill="red")

p8 = Canvas(window, width=80, height=60, bg="black")
p8.place(x=675, y=270)

p8.create_text(40, 15, text="BOT 8", font=("Arial Bold", 14), fill="red")

back = Canvas(window, width = 200, height = 200, bg = "green", borderwidth = -2)
back.place(x = -5, y = 385)

c1 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
c1.place(x=5, y=390)

pilImage = Image.open(card_texture[0])
image6 = ImageTk.PhotoImage(pilImage)
imagesprite6 = c1.create_image(42, 53, image=image6)


c2 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
c2.place(x=105, y=390)

h2_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h2_1.place(x = 82, y = 333)

pilImage = Image.open(card_texture_small[0])
image2_1 = ImageTk.PhotoImage(pilImage)
imagesprite2_1 = h2_1.create_image(18, 27, image=image2_1)

h2_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h2_2.place(x = 125, y = 333)

pilImage = Image.open(card_texture_small[0])
image2_2 = ImageTk.PhotoImage(pilImage)
imagesprite2_2 = h2_2.create_image(18, 27, image=image2_2)

p_ch = Label(window, font = "Arail 14", bg = "black", fg = "red", text = "Your chips: 1000")
p_ch.place(x = 250, y = 400)

p_bet = Label(window, font = "Arial 22", bg = "green", fg = "yellow", text = "none")
p_bet.place(x = 380, y = 330)
win_p_t = Label(window, font = "Arial 12", bg = "black", fg = "red", text = "Win probability is: ")
win_p_t.place(x = 5, y = 5)

win_p = Label(window, font = "Arial 12", bg = "black", fg = "red", text = "")
win_p.place(x = 5, y = 27)

h3_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h3_1.place(x = 62, y = 163)

pilImage = Image.open(card_texture_small[0])
image3_1 = ImageTk.PhotoImage(pilImage)
imagesprite3_1 = h3_1.create_image(18, 27, image=image3_1)

h3_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h3_2.place(x = 105, y = 163)

pilImage = Image.open(card_texture_small[0])
image3_2 = ImageTk.PhotoImage(pilImage)
imagesprite3_2 = h3_2.create_image(18, 27, image=image3_2)

h4_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h4_1.place(x = 182, y = 68)

pilImage = Image.open(card_texture_small[0])
image4_1 = ImageTk.PhotoImage(pilImage)
imagesprite4_1 = h4_1.create_image(18, 27, image=image4_1)

h4_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h4_2.place(x = 225, y = 68)

pilImage = Image.open(card_texture_small[0])
image4_2 = ImageTk.PhotoImage(pilImage)
imagesprite4_2 = h4_2.create_image(18, 27, image=image4_2)

h5_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h5_1.place(x = 300, y = 68)

pilImage = Image.open(card_texture_small[0])
image5_1 = ImageTk.PhotoImage(pilImage)
imagesprite5_1 = h5_1.create_image(18, 27, image=image5_1)

h5_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h5_2.place(x = 345, y = 68)

pilImage = Image.open(card_texture_small[0])
image5_2 = ImageTk.PhotoImage(pilImage)
imagesprite5_2 = h5_2.create_image(18, 27, image=image5_2)


h6_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h6_1.place(x = 440, y = 68)

pilImage = Image.open(card_texture_small[0])
image6_1 = ImageTk.PhotoImage(pilImage)
imagesprite6_1 = h6_1.create_image(18, 27, image=image6_1)

h6_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h6_2.place(x = 485, y = 68)

pilImage = Image.open(card_texture_small[0])
image6_2 = ImageTk.PhotoImage(pilImage)
imagesprite6_2 = h6_2.create_image(18, 27, image=image6_2)

h7_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h7_1.place(x = 562, y = 68)

pilImage = Image.open(card_texture_small[0])
image7_1 = ImageTk.PhotoImage(pilImage)
imagesprite7_1 = h7_1.create_image(18, 27, image=image7_1)

h7_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h7_2.place(x = 605, y = 68)

pilImage = Image.open(card_texture_small[0])
image7_2 = ImageTk.PhotoImage(pilImage)
imagesprite7_2 = h7_2.create_image(18, 27, image=image7_2)

h8_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h8_1.place(x = 682, y = 133)

pilImage = Image.open(card_texture_small[0])
image8_1 = ImageTk.PhotoImage(pilImage)
imagesprite8_1 = h8_1.create_image(18, 27, image=image8_1)

h8_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h8_2.place(x = 725, y = 133)

h9_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h9_1.place(x = 677, y = 333)

pilImage = Image.open(card_texture_small[0])
image9_1 = ImageTk.PhotoImage(pilImage)
imagesprite9_1 = h9_1.create_image(18, 27, image=image9_1)

h9_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h9_2.place(x = 720, y = 333)


bank = Label(window, font  = "Arial 32", text = "BANK:", bg = "green", fg = "yellow")
bank.place(x = 270, y = 260)


pilImage = Image.open(card_texture_small[0])
image9_2 = ImageTk.PhotoImage(pilImage)
imagesprite9_2 = h9_2.create_image(18, 27, image=image9_2)

pilImage = Image.open(card_texture_small[0])
image8_2 = ImageTk.PhotoImage(pilImage)
imagesprite8_2 = h8_2.create_image(18, 27, image=image8_2)

pilImage = Image.open(card_texture[0])
image7 = ImageTk.PhotoImage(pilImage)
imagesprite7 = c2.create_image(42, 53, image=image7)

ch1 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch1.place(x = 90, y = 295)
ch2 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch2.place(x = 70, y = 127)
ch3 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch3.place(x = 190, y = 30)
ch4 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch4.place(x = 312, y = 30)
ch5 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch5.place(x = 450, y = 30)
ch6 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch6.place(x = 570, y = 30)
ch7 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch7.place(x = 690, y = 96)
ch8 = Label(window, text = "none", font = "Arial 18", fg = "green", bg = "black")
ch8.place(x = 685, y = 295)
b_b_1 = Label(window, text = "none", font = "Arial 14", fg = "yellow", bg = "green")
b_b_1.place(x = 170, y = 260)
b_b_2 = Label(window, text = "none", font = "Arial 14", fg = "yellow", bg = "green")
b_b_2.place(x = 145, y = 180)
b_b_3 = Label(window, text = "none", font = "Arial 12", fg = "yellow", bg = "green")
b_b_3.place(x = 200, y = 121)
b_b_4 = Label(window, text = "none", font = "Arial 12", fg = "yellow", bg = "green")
b_b_4.place(x = 320, y = 121)
b_b_5 = Label(window, text = "none", font = "Arial 12", fg = "yellow", bg = "green")
b_b_5.place(x = 460, y = 121)
b_b_6 = Label(window, text = "none", font = "Arial 12", fg = "yellow", bg = "green")
b_b_6.place(x = 580, y = 121)
b_b_7 = Label(window, text = "none", font = "Arial 14", fg = "yellow", bg = "green")
b_b_7.place(x = 680, y = 190)
b_b_8 = Label(window, text = "none", font = "Arial 14", fg = "yellow", bg = "green")
b_b_8.place(x = 620, y = 280)

##-------------------------------------------
##+++++++++++++++++++++++++++++++++++++++++++
##-------------------------------------------


slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, length=200, width=19, bg="black", fg="red",
               font=("Arial Bold", 14))
slider.place(x=545, y=429)

##k = int(input("Введите количество игроков: "))

def loop():
    print("THAT WORKS!!!!!!")
    prev_bet = 0
    global temporary

    temporary = -1



    btn_raise = Button(window, text="Raise", bg="black", fg="red", font=("Arial Bold", 14),
                       command=lambda: player_bet(3))
    btn_call = Button(window, text="Call", bg="black", fg="red", font=("Arial Bold", 14), command=lambda: player_bet(1))
    btn_check = Button(window, text="Check/Fold", bg="black", fg="red", font=("Arial Bold", 14),
                       command=lambda: player_bet(2))

    btn_raise.place(width=100, height=50, x=450, y=430)
    btn_call.place(width=100, height=50, x=340, y=430)
    btn_check.place(width=100, height=50, x=230, y=430)

    k = 9

    data_chips = [1000] * (k + 1)

    chips_cfg(data_chips)
    print(data_chips)

    data_chips[0] = 0

    blind = 10

    dealer_pos = k

    data_ingame = [1] * (k + 1)

    data_ingame[0] = 0

    f1 = False

    g = 0
    while data_chips.count(0) < k:

        data_bets = []

        data_ingame = [0] * (k + 1)

        for i in range(1, k + 1):

            if data_chips[i] > 0:
                data_ingame[i] = 1

        data_pots = []

        for i in range(k + 1):

            data_pots.append([])

            for j in range(k + 1):
                data_pots[i].append(0)

        data_pots[0][0] = -1

        g += 1

        data_cards = new_hand(k)

        pilImage = Image.open(card_texture[data_cards[0]])
        image6 = ImageTk.PhotoImage(pilImage)
        imagesprite6 = c1.create_image(42, 53, image=image6)

        pilImage = Image.open(card_texture[data_cards[1]])
        image7 = ImageTk.PhotoImage(pilImage)
        imagesprite7 = c2.create_image(42, 53, image=image7)

        print(data_cards)
        print(card_texture)

        f = False

        while f == False:

            dealer_pos += 1

            if dealer_pos == k + 1:  # Передаем дилера следующему игроку

                dealer_pos = 1

            if data_chips[dealer_pos] != 0:
                f = True

        data_bets = [0] * (k + 1)

        f = False

        next_move = dealer_pos

        while f == False:  # Ставим малый блайнд

            next_move = next_move + 1

            if next_move == k + 1:
                next_move = 1

            if data_chips[next_move] != 0:

                data_bets[next_move] = blind

                if data_chips[next_move] < blind:

                    data_bets[next_move] = data_chips[next_move]

                    data_chips[next_move] = 0

                    data_ingame[next_move] = 2

                else:

                    data_chips[next_move] -= blind

                f = True
                bets_cfg(data_bets)
                chips_cfg(data_chips)
                p_ch.configure(text="Your chips: " + str(data_chips[1]))
                p_bet.configure(text= str(data_bets[1]))

        f = False

        while f == False:  # Ставим большой блайнд

            next_move = next_move + 1

            if next_move == k + 1:
                next_move = 1

            if data_chips[next_move] != 0:

                data_bets[next_move] = blind * 2

                if data_chips[next_move] < blind * 2:

                    data_bets[next_move] = data_chips[next_move]

                    data_chips[next_move] = 0

                    data_ingame[next_move] = 2

                else:

                    data_chips[next_move] -= blind * 2

                f = True
                bets_cfg(data_bets)
                chips_cfg(data_chips)
                bank.configure(text="BANK: " + str(sum(data_bets)))
                p_ch.configure(text="Your chips: " + str(data_chips[1]))
                p_bet.configure(text=str(data_bets[1]))

        bet = 20  # Разница в ставках

        prev_bet = 20  # Предыдущая ставка

        f = False  # Цикл ставок, пока все не уровняют

        f1 = False

        s = 0

        s_players = data_ingame.count(1)

        while f == False and f1 == False:

            f = True

            next_move = next_move + 1

            if next_move == k + 1:
                next_move = 1

            if data_ingame[next_move] == 1:

                s += 1

                if next_move != 1:

                    t = bot_preflop(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], bet, prev_bet,
                                    data_chips[next_move], data_bets[next_move])

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0

                    else:

                        data_chips[next_move] -= (t - data_bets[next_move])

                        if t - prev_bet > 0:

                            if bet <= t - prev_bet:
                                bet = t - prev_bet

                            prev_bet = t

                        data_bets[next_move] = t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

                    print("pevbet", prev_bet)

                    print(next_move, t, data_chips[next_move], data_bets[next_move])

                    print(data_ingame)

                if next_move == 1:

                    ##t = int(input("Введите ставку "))
                    t = temporary
                    while t == -1:
                        time.sleep(1)
                        t = temporary
                    temporary = -1
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet
                        else:
                            t = data_chips[1]

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0
                    else:

                        data_chips[next_move] -= t

                        if t + data_bets[next_move] - prev_bet > 0:

                            if t + data_bets[next_move] - prev_bet >= bet:
                                bet = t + data_bets[next_move] - prev_bet

                            prev_bet = t + data_bets[next_move]

                        data_bets[next_move] += t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))
            temp = []

            for i in range(1, k + 1):

                if data_ingame[i] == 1:
                    temp.append(data_bets[i])

            temp.sort()

            if len(temp) > 1:

                if temp[0] != temp[-1] or temp[0] < prev_bet or temp[-1] < prev_bet:
                    f = False

            if len(temp) == 1:

                if temp[0] < prev_bet:
                    f = False

            if s < s_players:
                f = False

            if data_ingame.count(1) < 2:

                if len(temp) > 0:

                    if temp[0] == prev_bet:
                        f1 = True

        print(data_ingame)

        print(data_chips)

        print(data_bets)

        data_pots = exchange(data_pots, data_bets, data_ingame, k)

        print(data_pots)

        ################################ FLOP ###############################

        print("---------------FLOP----------------")

        pilImage = Image.open(card_texture[data_cards[k * 2]])
        image1 = ImageTk.PhotoImage(pilImage)
        imagesprite1 = t1.create_image(42, 53, image=image1)

        pilImage = Image.open(card_texture[data_cards[k * 2 + 1]])
        image2 = ImageTk.PhotoImage(pilImage)
        imagesprite2 = t2.create_image(42, 53, image=image2)

        pilImage = Image.open(card_texture[data_cards[k * 2 + 2]])
        image3 = ImageTk.PhotoImage(pilImage)
        imagesprite3 = t3.create_image(42, 53, image=image3)
        print("etogo kazinooooo")
        for i in range(1, k + 1):
            data_ingame[i] = data_pots[0][i]

        data_flop = []

        data_flop.append(data_cards[k * 2])

        data_flop.append(data_cards[k * 2 + 1])

        data_flop.append(data_cards[k * 2 + 2])

        print('Ваша вероятность победы: ', win_prob_flop(k, data_cards, data_ingame))
        win_p.configure(text = str(win_prob_flop(k, data_cards, data_ingame)))

        prev_bet = 0

        bet = blind * 2

        f = False

        next_move = dealer_pos

        data_bets = [0] * (k + 1)

        s = 0

        s_players = data_ingame.count(1)

        while f == False and f1 == False:

            f = True

            next_move = next_move + 1

            if next_move == k + 1:
                next_move = 1

            if data_ingame[next_move] == 1:

                s += 1

                if next_move != 1:

                    t = bot_flop(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], data_flop, bet, prev_bet,
                                 data_chips[next_move], data_bets[next_move])

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0

                    else:

                        data_chips[next_move] -= (t - data_bets[next_move])

                        if t - prev_bet > 0:

                            if t - prev_bet >= bet:
                                bet = t - prev_bet

                            prev_bet = t

                        data_bets[next_move] = t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

                    print(next_move, t, data_chips[next_move], data_bets[next_move])

                    print(data_ingame)

                if next_move == 1:

                    print("у вас имеется ", data_chips[next_move], " фишек. Чтобы уровнять, нужно еще поствить ",
                          prev_bet - data_bets[1], ". Поднимать можно от ", bet + prev_bet, " фишек")

                    t = temporary
                    print("t", t)
                    while t == -1:
                        time.sleep(1)
                        t = temporary
                    temporary = -1
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet
                        else:
                            t = data_chips[1]

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0

                    else:

                        data_chips[next_move] -= t

                        if t + data_bets[next_move] - prev_bet > 0:

                            if bet <= t + data_bets[next_move] - prev_bet:
                                bet = t + data_bets[next_move] - prev_bet

                            prev_bet = t + data_bets[next_move]

                        data_bets[next_move] += t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

            temp = []

            print("prev bet ", prev_bet)

            for i in range(1, k + 1):

                if data_ingame[i] == 1:
                    temp.append(data_bets[i])

            temp.sort()

            if len(temp) > 1:

                if temp[0] != temp[-1] or temp[0] < prev_bet or temp[-1] < prev_bet:
                    f = False

            if len(temp) == 1:

                if temp[0] < prev_bet:
                    f = False

            if s < s_players:
                f = False

            if data_ingame.count(1) < 2:

                if len(temp) > 0:

                    if temp[0] == prev_bet:
                        f1 = True

        print(data_ingame)

        print(data_chips)

        print(data_bets)

        data_pots = exchange(data_pots, data_bets, data_ingame, k)

        print(data_pots)

        ############################# TURN #########################

        print("---------------------- TURN -----------------")

        print(data_cards[k * 2 + 3])

        pilImage = Image.open(card_texture[data_cards[k * 2 + 3]])
        image4 = ImageTk.PhotoImage(pilImage)
        imagesprite4 = t4.create_image(42, 53, image=image4)

        for i in range(1, k + 1):
            data_ingame[i] = data_pots[0][i]

        print('Ваша вероятность победы: ', win_prob_turn(k, data_cards, data_ingame))
        win_p.configure(text = str(win_prob_turn(k, data_cards, data_ingame)))
        data_turn = []

        data_turn.extend(data_flop)

        data_turn.append(data_cards[k * 2 + 3])

        prev_bet = 0

        bet = blind * 2

        f = False

        next_move = dealer_pos

        data_bets = [0] * (k + 1)

        s = 0

        s_players = data_ingame.count(1)

        while f == False and f1 == False:

            f = True

            next_move = next_move + 1

            if next_move == k + 1:
                next_move = 1

            if data_ingame[next_move] == 1:

                s += 1

                if next_move != 1:

                    t = bot_turn(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], data_turn, bet, prev_bet,
                                 data_chips[next_move], data_bets[next_move])

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0

                    else:

                        data_chips[next_move] -= (t - data_bets[next_move])

                        if t - prev_bet > 0:

                            if t - prev_bet >= bet:
                                bet = t - prev_bet

                            prev_bet = t

                        data_bets[next_move] = t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

                    print(next_move, t, data_chips[next_move], data_bets[next_move])

                    print(data_ingame)
                if next_move == 1:
                    print("у вас имеется ", data_chips[next_move], " фишек. Чтобы уровнять, нужно еще поствить ",
                          prev_bet - data_bets[1], ". Поднимать можно от ", bet + prev_bet, " фишек")
                    print(temporary)
                    t = temporary
                    while t == -1:
                        time.sleep(1)
                        t = temporary

                    temporary = -1
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet
                        else:
                            t = data_chips[1]
                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0

                    else:

                        data_chips[next_move] -= t

                        if t + data_bets[next_move] - prev_bet > 0:

                            if t + data_bets[next_move] - prev_bet >= bet:
                                bet = t + data_bets[next_move] - prev_bet

                            prev_bet = t + data_bets[next_move]

                        data_bets[next_move] += t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

            temp = []

            print("prev bet ", prev_bet)

            for i in range(1, k + 1):

                if data_ingame[i] == 1:
                    temp.append(data_bets[i])

            temp.sort()

            if len(temp) > 1:

                if temp[0] != temp[-1] or temp[0] < prev_bet or temp[-1] < prev_bet:
                    f = False

            if len(temp) == 1:

                if temp[0] < prev_bet:
                    f = False

            if s < s_players:
                f = False

            if data_ingame.count(1) < 2:

                if len(temp) > 0:

                    if temp[0] == prev_bet:
                        f1 = True

        print(data_ingame)

        print(data_chips)

        print(data_bets)

        data_pots = exchange(data_pots, data_bets, data_ingame, k)

        print(data_pots)

        ############################# RIVER #########################

        print("---------------------- RIVER -----------------")

        print(data_cards[k * 2 + 4])

        pilImage = Image.open(card_texture[data_cards[k * 2  +4]])
        image5 = ImageTk.PhotoImage(pilImage)
        imagesprite5 = t5.create_image(42, 53, image=image5)

        for i in range(1, k + 1):
            data_ingame[i] = data_pots[0][i]

        data_reaver = []

        data_reaver.extend(data_turn)

        data_reaver.append(data_cards[k * 2 + 3])

        prev_bet = 0
        win_p.configure(text="hidden")
        bet = blind * 2

        f = False

        next_move = dealer_pos

        data_bets = [0] * (k + 1)

        s = 0

        s_players = data_ingame.count(1)

        while f == False and f1 == False:

            f = True

            next_move = next_move + 1

            if next_move == k + 1:
                next_move = 1

            if data_ingame[next_move] == 1:

                s += 1

                if next_move != 1:

                    t = bot_reaver(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], data_reaver, bet, prev_bet,
                                   data_chips[next_move], data_bets[next_move])

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0

                    else:

                        data_chips[next_move] -= (t - data_bets[next_move])

                        if t - prev_bet > 0:

                            if t - prev_bet >= bet:
                                bet = t - prev_bet

                            prev_bet = t

                        data_bets[next_move] = t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))

                    print(next_move, t, data_chips[next_move], data_bets[next_move])

                    print(data_ingame)

                if next_move == 1:

                    print("у вас имеется ", data_chips[next_move], " фишек. Чтобы уровнять, нужно еще поствить ",
                          prev_bet - data_bets[1], ". Поднимать можно от ", bet + prev_bet, " фишек")

                    t = temporary
                    temporary = -1
                    while t == -1:
                        time.sleep(1)
                        t = temporary
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet
                        else:
                            t = data_chips[1]

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0

                    else:

                        data_chips[next_move] -= t

                        if t + data_bets[next_move] - prev_bet > 0:

                            if t + data_bets[next_move] - prev_bet >= bet:
                                bet = t + data_bets[next_move] - prev_bet

                            prev_bet = t + data_bets[next_move]

                        data_bets[next_move] += t

                        if data_chips[next_move] == 0:
                            data_ingame[next_move] = 2
                    bets_cfg(data_bets)
                    chips_cfg(data_chips)
                    bank.configure(text="BANK: " + str(sum(data_bets)))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))

            temp = []

            print("prev bet ", prev_bet)

            for i in range(1, k + 1):

                if data_ingame[i] == 1:
                    temp.append(data_bets[i])

            temp.sort()

            if len(temp) > 1:

                if temp[0] != temp[-1] or temp[0] < prev_bet or temp[-1] < prev_bet:
                    f = False

            if len(temp) == 1:

                if temp[0] < prev_bet:
                    f = False

            if s < s_players:
                f = False

            if data_ingame.count(1) < 2:

                if len(temp) > 0:

                    if temp[0] == prev_bet:
                        f1 = True

        print(data_ingame)

        print(data_chips)

        print(data_bets)

        data_pots = exchange(data_pots, data_bets, data_ingame, k)

        print(data_pots)

        print("==============================================")

        data_pots = after_exchange(data_pots, data_bets, data_ingame, k)

        print(data_pots)

        print("==============================================")

        print("==============================================")

        print(card_texture_small)

        pilImage = Image.open(card_texture_small[data_cards[3]])
        image10 = ImageTk.PhotoImage(pilImage)
        imagesprite10 = h2_1.create_image(20, 26, image=image10)

        pilImage = Image.open(card_texture_small[data_cards[4]])
        image11 = ImageTk.PhotoImage(pilImage)
        imagesprite11 = h2_2.create_image(20, 26, image=image11)

        pilImage = Image.open(card_texture_small[data_cards[5]])
        image12 = ImageTk.PhotoImage(pilImage)
        imagesprite12 = h3_1.create_image(20, 26, image=image12)

        pilImage = Image.open(card_texture_small[data_cards[6]])
        image13 = ImageTk.PhotoImage(pilImage)
        imagesprite13 = h3_2.create_image(20, 26, image=image13)

        pilImage = Image.open(card_texture_small[data_cards[7]])
        image14 = ImageTk.PhotoImage(pilImage)
        imagesprite14 = h4_1.create_image(20, 26, image=image14)

        pilImage = Image.open(card_texture_small[data_cards[8]])
        image15 = ImageTk.PhotoImage(pilImage)
        imagesprite15 = h4_2.create_image(20, 26, image=image15)

        pilImage = Image.open(card_texture_small[data_cards[9]])
        image16 = ImageTk.PhotoImage(pilImage)
        imagesprite16 = h5_1.create_image(20, 26, image=image16)

        pilImage = Image.open(card_texture_small[data_cards[10]])
        image17 = ImageTk.PhotoImage(pilImage)
        imagesprite17 = h5_2.create_image(20, 26, image=image17)

        pilImage = Image.open(card_texture_small[data_cards[11]])
        image18 = ImageTk.PhotoImage(pilImage)
        imagesprite18 = h6_1.create_image(20, 26, image=image18)
        pilImage = Image.open(card_texture_small[data_cards[12]])
        image19 = ImageTk.PhotoImage(pilImage)
        imagesprite19 = h6_2.create_image(20,26, image=image19)

        pilImage = Image.open(card_texture_small[data_cards[13]])
        image20 = ImageTk.PhotoImage(pilImage)
        imagesprite20 = h7_1.create_image(20, 26, image=image20)

        pilImage = Image.open(card_texture_small[data_cards[14]])
        image21 = ImageTk.PhotoImage(pilImage)
        imagesprite21 = h7_2.create_image(20, 26, image=image21)

        pilImage = Image.open(card_texture_small[data_cards[15]])
        image22 = ImageTk.PhotoImage(pilImage)
        imagesprite22 = h8_1.create_image(20, 26, image=image22)

        pilImage = Image.open(card_texture_small[data_cards[16]])
        image23 = ImageTk.PhotoImage(pilImage)
        imagesprite23 = h8_2.create_image(20, 26, image=image23)

        pilImage = Image.open(card_texture_small[data_cards[17]])
        image24 = ImageTk.PhotoImage(pilImage)
        imagesprite24 = h9_1.create_image(20, 26, image=image24)

        pilImage = Image.open(card_texture_small[data_cards[18]])
        image25 = ImageTk.PhotoImage(pilImage)
        imagesprite25 = h9_2.create_image(20, 26, image=image25)

        time.sleep(10)

        pilImage = Image.open(card_texture_small[0])
        image10 = ImageTk.PhotoImage(pilImage)
        imagesprite10 = h2_1.create_image(20, 26, image=image10)

        pilImage = Image.open(card_texture_small[0])
        image11 = ImageTk.PhotoImage(pilImage)
        imagesprite11 = h2_2.create_image(20, 26, image=image11)

        pilImage = Image.open(card_texture_small[0])
        image12 = ImageTk.PhotoImage(pilImage)
        imagesprite12 = h3_1.create_image(20, 26, image=image12)

        pilImage = Image.open(card_texture_small[0])
        image13 = ImageTk.PhotoImage(pilImage)
        imagesprite13 = h3_2.create_image(20, 26, image=image13)

        pilImage = Image.open(card_texture_small[0])
        image14 = ImageTk.PhotoImage(pilImage)
        imagesprite14 = h4_1.create_image(20, 26, image=image14)

        pilImage = Image.open(card_texture_small[0])
        image15 = ImageTk.PhotoImage(pilImage)
        imagesprite15 = h4_2.create_image(20, 26, image=image15)

        pilImage = Image.open(card_texture_small[0])
        image16 = ImageTk.PhotoImage(pilImage)
        imagesprite16 = h5_1.create_image(20, 26, image=image16)

        pilImage = Image.open(card_texture_small[0])
        image17 = ImageTk.PhotoImage(pilImage)
        imagesprite17 = h5_2.create_image(20, 26, image=image17)

        pilImage = Image.open(card_texture_small[0])
        image18 = ImageTk.PhotoImage(pilImage)
        imagesprite18 = h6_1.create_image(20, 26, image=image18)

        pilImage = Image.open(card_texture_small[0])
        image19 = ImageTk.PhotoImage(pilImage)
        imagesprite19 = h6_2.create_image(20, 26, image=image19)

        pilImage = Image.open(card_texture_small[0])
        image20 = ImageTk.PhotoImage(pilImage)
        imagesprite20 = h7_1.create_image(20, 26, image=image20)

        pilImage = Image.open(card_texture_small[0])
        image21 = ImageTk.PhotoImage(pilImage)
        imagesprite21 = h7_2.create_image(20, 26, image=image21)

        pilImage = Image.open(card_texture_small[0])
        image22 = ImageTk.PhotoImage(pilImage)
        imagesprite22 = h8_1.create_image(20, 26, image=image22)

        pilImage = Image.open(card_texture_small[0])
        image23 = ImageTk.PhotoImage(pilImage)
        imagesprite23 = h8_2.create_image(20, 26, image=image23)

        pilImage = Image.open(card_texture_small[0])
        image24 = ImageTk.PhotoImage(pilImage)
        imagesprite24 = h9_1.create_image(20, 26, image=image24)

        pilImage = Image.open(card_texture_small[0])
        image25 = ImageTk.PhotoImage(pilImage)
        imagesprite25 = h9_2.create_image(20, 26, image=image25)

        data_win = [0]

        for i in range(1, k + 1):
            data_win.append(winner(i, data_cards, k))

        k_pots = 0

        for i in data_pots[1:]:

            kk = 0

            if i.count(0) < k:

                m = 0

                for j in range(1, k + 1):

                    if i[j] == 1:

                        if data_win[j] > m:
                            m = data_win[j]

                for j in range(1, k + 1):

                    if i[j] == 1:

                        if data_win[j] == m:
                            kk += 1

                for j in range(1, k + 1):

                    if i[j] == 1:

                        if data_win[j] == m:
                            data_chips[j] += i[0] // kk

                            t = "Player " + str(j) + " wins " + str(i[0] // kk) + " chips!!!"

                            print(t)
        pilImage = Image.open(card_texture[0])
        image1 = ImageTk.PhotoImage(pilImage)
        imagesprite1 = t1.create_image(42, 53, image=image1)

        pilImage = Image.open(card_texture[0])
        image2 = ImageTk.PhotoImage(pilImage)
        imagesprite2 = t2.create_image(42, 53, image=image2)

        pilImage = Image.open(card_texture[0])
        image3 = ImageTk.PhotoImage(pilImage)
        imagesprite3 = t3.create_image(42, 53, image=image3)

        pilImage = Image.open(card_texture[0])
        image4 = ImageTk.PhotoImage(pilImage)
        imagesprite4 = t4.create_image(42, 53, image=image4)

        pilImage = Image.open(card_texture[0])
        image5 = ImageTk.PhotoImage(pilImage)
        imagesprite5 = t5.create_image(42, 53, image=image5)


my_thread = threading.Thread(target=loop)
my_thread.start()

mainloop()

# if g > 10:

# break
