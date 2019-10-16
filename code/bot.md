# Набор функций, которые отвечают за действия ботов(Рандома больше чем теорвера :octocat::octocat::octocat:)
1. card1, card2 - карты игрока(бота)
2. bet - разница между последними двумя изменениями ставок
3. chips - кол-во фишек игрока(бота)
4. data_flop, data_turn, data_reaver - массивы с картами на столе
### 

```python
from ranom import random
def bot_preflop(card1, card2, bet, chips): 
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
