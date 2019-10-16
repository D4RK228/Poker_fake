# Функции, связанные с раздачей карт и переводом фишек
1. new_hand - раздача
2. after_reaver - разбивает все фишки на поты после каждого кона
(Это нужно чтобы игрок, который пошел ва-банк не купил себе лишний Porsche 911)
3. exchange - Выявляет победителя внутри каждого пота (Если их несколько, выигрыш делится поровну)
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
```
