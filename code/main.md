```python
from random import random
def new_hand(k_player):
    data_cards = []
    for i in range(k_player*2 + 5):
        f = False
        while f == False:
            n = int(random()*51 + 1)
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
        for j in range(1, k_player+1):
            if(data_pots[i][j] == 1):
                if winner(j, data_cards, k_player) > max:
                    max = winner(j, data_cards, k_player)
        kol = 0
        for j in range(1, k_player+1):
            if(data_pots[i][j] == 1):
                if winner(j, data_cards, k_player) == max:
                    kol += 1
        for j in range(1, k_player+1):
            if(data_pots[i][j] == 1):
                if winner(j, data_cards, k_player) == max:
                    data_chips[j] += int(data_pots[i][0]/kol)
    return data_chips


def straight_flash(player, data_cards, k_player):
    data_comb = []   #комбинация игрока
    data_comb_n = []    #номиналы комбинции
    data_comb_m = []    #масти комбинации
    data_comb.append(data_cards[player*2 - 2])
    data_comb.append(data_cards[player*2 - 1])
    s = 0
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb_m.append((data_comb[i] - 1) // 13 + 1)
    data_comb_m.sort()
    for i in range(3):
        if data_comb_m[i] == data_comb_m[i+1] and data_comb_m[i] == data_comb_m[i+2] and data_comb_m[i] == data_comb_m[i+3] and data_comb_m[i] == data_comb_m[i+4]:
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
        print(data_comb_n)
        a = 0
        for i in range(len(data_comb_n) - 4):
            if data_comb_n[i] == data_comb_n[i+1] - 1 and data_comb_n[i] == data_comb_n[i+2] - 2 and data_comb_n[i] == data_comb_n[i+3] - 3 and data_comb_n[i] == data_comb_n[i+4] - 4:
                a = data_comb_n[i + 4]
        return a
    
def straight(player, data_cards, k_player):
    data_comb = []
    data_comb.append(data_cards[player*2 - 1])
    data_comb.append(data_cards[player*2 - 2])
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb[i] = data_comb[i] % 13
    for i in range(7):
        if(data_comb[i] == 0):
            data_comb.append(13)
    data_comb.sort()
    f = True
    while f == True:
        for i in range(len(data_comb) - 1):
            f = False
            if data_comb[i] == data_comb[i+1]:
                data_comb.pop(i)
                f = True
                break
    s = 0
    if len(data_comb) >= 5:
        for i in range(len(data_comb) - 4):
            if data_comb[i] == data_comb[i+1] - 1 and data_comb[i] == data_comb[i+2] - 2 and data_comb[i] == data_comb[i+3] - 3 and data_comb[i] == data_comb[i+4] - 4:
                s = data_comb[i + 4]
    return s


def flash(player, data_cards, k_player):
    data_comb = []   #комбинация игрока
    data_comb_n = []    #номиналы комбинции
    data_comb_m = []    #масти комбинации
    data_comb.append(data_cards[player*2 - 2])
    data_comb.append(data_cards[player*2 - 1])
    s = 0
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    
    for i in range(7):
        data_comb_m.append((data_comb[i] - 1) // 13 + 1)
    for i in range(7):
        if(data_comb[i] == 0):
            data_comb[i] = 13
    data_comb_m.sort()
    for i in range(3):
        if data_comb_m[i] == data_comb_m[i+1] and data_comb_m[i] == data_comb_m[i+2] and data_comb_m[i] == data_comb_m[i+3] and data_comb_m[i] == data_comb_m[i+4]:
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
    data_comb.append(data_cards[player*2 - 1])
    data_comb.append(data_cards[player*2 - 2])
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb[i] = data_comb[i] % 13
    for i in range(7):
        if(data_comb[i] == 0):
            data_comb[i] = 13
    data_comb.sort()
    s = 0
    for i in range(len(data_comb) - 3):
        if data_comb[i] == data_comb[i+3]:
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
    data_comb.append(data_cards[player*2 - 1])
    data_comb.append(data_cards[player*2 - 2])
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb[i] = data_comb[i] % 13
    for i in range(7):
        if(data_comb[i] == 0):
            data_comb[i] = 13
    data_comb.sort()
    data_comb.reverse()
    s = 0
    for i in range(5):
        if data_comb[i] == data_comb[i+2]:
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
        if data_comb[i] == data_comb[i+1]:
            a = data_comb[i]
            break
    if a!= 0 and s != 0:
        s += a
        return s
    else:
        return 0
    
def three(player, data_cards, k_player):
    data_comb = []
    data_comb.append(data_cards[player*2 - 1])
    data_comb.append(data_cards[player*2 - 2])
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb[i] = data_comb[i] % 13
    for i in range(7):
        if(data_comb[i] == 0):
            data_comb[i] = 13
    data_comb.sort()
    data_comb.reverse()
    s = 0
    for i in range(5):
        if data_comb[i] == data_comb[i+2]:
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
    data_comb.append(data_cards[player*2 - 1])
    data_comb.append(data_cards[player*2 - 2])
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb[i] = data_comb[i] % 13
    for i in range(7):
        if(data_comb[i] == 0):
            data_comb[i] = 13
    data_comb.sort()
    data_comb.reverse()
    s = 0
    for i in range(6):
        if data_comb[i] == data_comb[i+1]:
            s = data_comb[i]
            data_comb[i] = -1
            data_comb[i+1] = -1
            break
    data_comb.sort()
    data_comb.reverse()
    a = 0
    for i in range(6):
        if data_comb[i] == data_comb[i+1] and data_comb[i] != -1:
            a = data_comb[i]
            data_comb[i] = -1
            data_comb[i+1] = -1
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
    data_comb.append(data_cards[player*2 - 1])
    data_comb.append(data_cards[player*2 - 2])
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb[i] = data_comb[i] % 13
    for i in range(7):
        if(data_comb[i] == 0):
            data_comb[i] = 13
    data_comb.sort()
    data_comb.reverse()
    s = 0
    for i in range(6):
        if data_comb[i] == data_comb[i+1]:
            s = data_comb[i]
            data_comb[i] = -1
            data_comb[i+1] = -1
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
    data_comb.append(data_cards[player*2 - 1])
    data_comb.append(data_cards[player*2 - 2])
    for i in range(5):
        data_comb.append(data_cards[k_player*2 + i])
    for i in range(7):
        data_comb[i] = data_comb[i] % 13
    for i in range(7):
        if(data_comb[i] == 0):
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
        return(900000000000 + straight_flash(k, data_cards, k_player))
    elif quards(k, data_cards, k_player) != 0:
        return(800000000000 + quards(k, data_cards, k_player))
    elif full_house(k, data_cards, k_player) != 0:
        return(700000000000 + full_house(k, data_cards, k_player))
    elif flash(k, data_cards, k_player) != 0:
        return(600000000000 + flash(k, data_cards, k_player))
    elif straight(k, data_cards, k_player) != 0:
        return(500000000000 + straight(k, data_cards, k_player))
    elif three(k, data_cards, k_player) != 0:
        return(400000000000 + three(k, data_cards, k_player))
    elif two_pairs(k, data_cards, k_player) != 0:
        return(300000000000 + two_pairs(k, data_cards, k_player))
    elif pair(k, data_cards, k_player) != 0:
        return(200000000000 + pair(k, data_cards, k_player))
    elif kicker(k, data_cards, k_player) != 0:
        return(100000000000 + kicker(k, data_cards, k_player))
    
def exchange(data_pots, data_bet, data_ingame, data_chips, k_player):
    min = -1
    max = -1
    k_pots = 1
    if data_pots[0][0] == 0:
        for j in range(1, k_player + 1):
            if data_ingame[j] == 0:
                data_pots[0][j] = 0
    if data_pots[0][0] == -1:
        data_pots[0][0] = 0
        for j in range(1, k_player + 1):
            data_pots[0][j] = data_ingame[j]
    for i in range(2, k_player+1):
        if data_pots[i][0] == 0:
            break
        k_pots += 1
    for i in range(1, k_player+1):
        if data_pots[0][i] == 1:
            if min == -1:
                min = data_bet[i]
            if max == -1:
                max = data_bet[i]
            if data_bet[i] < min:
                min = data_bet[i]
            if data_bet[i] > max:
                max = data_bet[i]
    
    while min != max:
        sum = 0
        for i in range(1, k_player + 1):
            if data_bet[i] <= min:
                sum += data_bet[i]
                data_bet[i] = 0
            else:
                sum += min
                data_bet[i] -= min
            if data_bet[i] == 0 and data_chips[i] == 0 and data_pots[0][i] == 1:
                data_pots[k_pots][i] = 1
                data_pots[0][i] = 2
            if data_pots[0][i] == 1 and (data_chips[i] > 0 or data_bet[i] > 0):
                data_pots[k_pots][i] = 1
        data_pots[k_pots][0] += sum
        k_pots += 1
        
        min = -1
        max = -1
        for i in range(1, k_player + 1):
            if data_pots[0][i] == 1:
                if min == -1 and data_bet[i] != 0:
                    min = data_bet[i]
                if max == -1 and data_bet[i] != 0:
                    max = data_bet[i]
                if data_bet[i] < min and data_bet[i] != 0:
                    min = data_bet[i]
                if data_bet[i] > max and data_bet[i] != 0:
                    max = data_bet[i]
            
    
        
        
    for i in range(1, k_player + 1):
        data_pots[k_pots][0] += data_bet[i]
        if data_pots[0][i] == 1:
            data_pots[k_pots][i] = 1

    for i in range(1, k_player + 1):
        if data_pots[0][i] == 0:
            for j in range(1, k_pots + 1):
                data_pots[j][i] = 0
    return data_pots


def bot_preflop(card1, card2, bet, chips): # bet - разница между последними двумя изменениями ставок 
    x = card1 % 13
    y = card2 % 13
    if x == 0:
        x = 13
    if y == 0:
        y = 13
    if x + y >= 22:
        r = random()
        if r > 0.1:
            stavka = int(bet * (random()*2 + 2))
        else:
            stavka = bet
        if stavka > chips:
            return chips
        else:
            return stavka
    if x + y > 7 or x == y:
        r = random()
        if r < 0.15:
            return 0
        else:
            if r > 0.9:
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka
        
    if x + y <= 7:
        r = random()
        if r < 0.6:
            return 0
        else:
            if r > 0.95:
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka


def bot_flop(card1, card2, data_flop, bet, chips): #если никто не ставил, тогда bet = bigblind
    data_card = []
    data_card.append(card1)
    data_card.append(card2)
    data_card.extend(data_flop)
    f = False
    while f == False:
        f = True
        cardturn = random()*51 + 1
        if cardturn in data_card:
            f = False
    f = False
    data_card.append(cardturn)
    while f == False:
        f = True
        cardreaver = random()*51 + 1
        if cardreaver in data_card:
            f = False
    data_card.append(cardreaver)
    
    if winner(1, data_card, 1) < 200000000000:
        r = random()
        if r < 0.9:
            return 0
        else:
            if r > 0.98:
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka
                
    if winner(1, data_card, 1) < 500000000000:
        r = random()
        if r < 0.1:
            return 0
        else:
            if r > 0.7:
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka
    if winner(1, data_card, 1) >= 500000000000:
        r = random()
        if r > 0.1:
            stavka = int(bet * (random()*2 + 2))
        else:
            stavka = bet
        if stavka > chips:
            return chips
        else:
            return stavka

        
        
def bot_turn(card1, card2, data_turn, bet, chips):
    data_card = []
    data_card.append(card1)
    data_card.append(card2)
    data_card.extend(data_turn)
    f = False
    while f == False:
        f = True
        cardreaver = random()*51 + 1
        if cardreaver in data_card:
            f = False
    data_card.append(cardreaver)
    
    
    if winner(1, data_card, 1) < 300000000000:
        r = random()
        if r < 0.9:
            return 0
        else:
            if r > 0.98:
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka
                
    if winner(1, data_card, 1) < 600000000000:
        r = random()
        if r < 0.03:
            return 0
        else:
            if r > 0.7:
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka
    if winner(1, data_card, 1) >= 600000000000:
        r = random()
        if r > 0.1:
            stavka = int(bet * (random()*2 + 2))
        else:
            stavka = bet
        if stavka > chips:
            return chips
        else:
            return stavka

        
def bot_reaver(card1, card2, data_reaver, bet, chips):
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
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka
                
    if winner(1, data_card, 1) < 700000000000:
        r = random()
        if r < 0.1:
            return 0
        else:
            if r > 0.7:
                stavka = int(bet * (random() * 2 + 2))
                if stavka > chips:
                    return chips
                else:
                    return stavka
            else:
                stavka = bet
                if stavka > chips:
                    return chips
                else:
                    return stavka
    if winner(1, data_card, 1) >= 700000000000:
        r = random()
        if r > 0.1:
            stavka = int(bet * (random()*2 + 2))
        else:
            stavka = bet
        if stavka > chips:
            return chips
        else:
            return stavka
```
