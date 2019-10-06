```python
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
```
