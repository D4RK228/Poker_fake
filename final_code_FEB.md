
Ссылка на скринкаст: https://youtu.be/2ohxgG3biok

``` python
from random import random
from tkinter import *
from PIL import ImageTk, Image
import time
import threading
import PIL
from check import winner
from bot_func import *
from other_manip import *
from texture_data_fill import *
from cfg_ingame import *

def player_bet(a):
    global temporary
    global prev_bet
    if a == 1:
        temporary = -2
    if a == 2:
        temporary = -3
    if a == 3:
        temporary = -4


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


card_texture = texture_fill()
card_texture_small = texture_small_fill()

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

pilImage = Image.open(card_texture_small[0])
image8_2 = ImageTk.PhotoImage(pilImage)
imagesprite8_2 = h8_2.create_image(18, 27, image=image8_2)

h9_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h9_1.place(x = 677, y = 333)

pilImage = Image.open(card_texture_small[0])
image9_1 = ImageTk.PhotoImage(pilImage)
imagesprite9_1 = h9_1.create_image(18, 27, image=image9_1)

h9_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
h9_2.place(x = 720, y = 333)

pilImage = Image.open(card_texture_small[0])
image9_2 = ImageTk.PhotoImage(pilImage)
imagesprite9_2 = h9_2.create_image(18, 27, image=image9_2)



def create_hand_links():
    hand_links = []
    hand_links.append(h2_1)
    hand_links.append(h2_2)
    hand_links.append(h3_1)
    hand_links.append(h3_2)
    hand_links.append(h4_1)
    hand_links.append(h4_2)
    hand_links.append(h5_1)
    hand_links.append(h5_2)
    hand_links.append(h6_1)
    hand_links.append(h6_2)
    hand_links.append(h7_1)
    hand_links.append(h7_2)
    hand_links.append(h8_1)
    hand_links.append(h8_2)
    hand_links.append(h9_1)
    hand_links.append(h9_2)
    return hand_links


def create_image_links(data_cards):
    images = []
    for i in range(2, len(data_cards) - 5):
        images.append(ImageTk.PhotoImage(Image.open(card_texture_small[data_cards[i]])))
    return images


def create_image_links_f(x):
    images = []
    for i in range(2, x - 5):
        images.append(ImageTk.PhotoImage(Image.open("rubashka-fold.jpg")))
    return images

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

hand_links = create_hand_links()

c2 = Canvas(window, width=85, height=110, bg="green", borderwidth=-2)
c2.place(x=105, y=390)

p_ch = Label(window, font = "Arail 14", bg = "black", fg = "red", text = "Your chips: 1000")
p_ch.place(x = 250, y = 400)

p_bet = Label(window, font = "Arial 22", bg = "green", fg = "yellow", text = "none")
p_bet.place(x = 380, y = 330)
win_p_t = Label(window, font = "Arial 12", bg = "black", fg = "red", text = "Win probability is: ")
win_p_t.place(x = 5, y = 5)

win_p = Label(window, font = "Arial 12", bg = "black", fg = "red", text = "")
win_p.place(x = 5, y = 27)

bank = Label(window, font  = "Arial 32", text = "BANK:", bg = "green", fg = "yellow")
bank.place(x = 270, y = 260)



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

dealer = Label(window, font = "Arail 32", bg = "black", fg = "blue", text = "D")
dealer_data = [[420, 370], [40, 270], [20, 100], [140, 10], [270, 10], [405, 10], [525, 10], [645, 75], [645, 275]]
dealer.place(x = dealer_data[0][0], y = dealer_data[0][1])

def loop():
    prev_bet = 0
    global temporary
    temporary = -1

    bank_temp = 0

    def win_p_func():
        win_p.configure(text=(str(int(win_prob_flop(k, data_cards, data_ingame) * 100)) + " %"))
    def win_p_func_turn():
        win_p.configure(text=(str(int(win_prob_turn(k, data_cards, data_ingame) * 100)) + " %"))
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

    data_chips[0] = 0

    blind = 10

    dealer_pos = k

    data_ingame = [1] * (k + 1)

    data_ingame[0] = 0

    f1 = False

    g = 0
    while data_chips.count(0) < k:

        data_bets = []
        bank_temp = 0

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

        image_links = create_image_links(data_cards)
        image_links_f = create_image_links_f(len(data_cards))

        pilImage = Image.open(card_texture[data_cards[0]])
        image6 = ImageTk.PhotoImage(pilImage)
        imagesprite6 = c1.create_image(42, 53, image=image6)

        pilImage = Image.open(card_texture[data_cards[1]])
        image7 = ImageTk.PhotoImage(pilImage)
        imagesprite7 = c2.create_image(42, 53, image=image7)


        f = False

        while f == False:

            dealer_pos += 1

            if dealer_pos == k + 1:  # Передаем дилера следующему игроку

                dealer_pos = 1

            if data_chips[dealer_pos] != 0:
                f = True
        dealer.place(x=dealer_data[dealer_pos - 1][0], y=dealer_data[dealer_pos - 1][1])

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

        slider.configure(from_=prev_bet*2, to=data_chips[1])

        while f == False and f1 == False:

            f = True

            next_move = next_move + 1

            if next_move == k + 1:
                next_move = 1

            if data_ingame[next_move] == 1:

                s += 1

                if next_move != 1:
                    time.sleep(2)
                    t = bot_preflop(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], bet, prev_bet,
                                    data_chips[next_move], data_bets[next_move])

                    hand_links = create_hand_links()

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0
                                a = hand_links[next_move*2 - 3].create_image(18, 26, image=image_links_f[next_move * 2 - 3])
                                b = hand_links[next_move * 2 - 4].create_image(18, 26, image=image_links_f[next_move * 2 - 4])

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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

                if next_move == 1:
                    if prev_bet != 0 and data_chips[1] > prev_bet*2:
                        slider.configure(from_=prev_bet * 2, to=data_chips[1])
                    elif data_chips[1] > prev_bet*2:
                        slider.configure(from_=blind * 2, to=data_chips[1])
                    else:
                        slider.configure(from_=data_chips[1], to=data_chips[1])
                    ##t = int(input("Введите ставку "))
                    temporary = -1
                    t = temporary
                    while t == -1:
                        time.sleep(1)
                        t = temporary
                    temporary = -1
                    if t == -4:
                        if data_chips[1] <= prev_bet:
                            t = -2
                        else:
                            t = slider.get()
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet - data_bets[1]
                        else:
                            t = data_chips[1]


                    if t == -3:
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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
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

        bank_temp += sum(data_bets)
        data_pots = exchange(data_pots, data_bets, data_ingame, k)


        ################################ FLOP ###############################
        btn_win_prob = Button(window, text="show win \n probability", bg="black", fg="red", font=("Arial Bold", 14),
                              command=lambda: win_p_func())
        btn_win_prob.place(width=100, height=50, x=0, y=220)

        pilImage = Image.open(card_texture[data_cards[k * 2]])
        image1 = ImageTk.PhotoImage(pilImage)
        imagesprite1 = t1.create_image(42, 53, image=image1)

        pilImage = Image.open(card_texture[data_cards[k * 2 + 1]])
        image2 = ImageTk.PhotoImage(pilImage)
        imagesprite2 = t2.create_image(42, 53, image=image2)

        pilImage = Image.open(card_texture[data_cards[k * 2 + 2]])
        image3 = ImageTk.PhotoImage(pilImage)
        imagesprite3 = t3.create_image(42, 53, image=image3)
        for i in range(1, k + 1):
            data_ingame[i] = data_pots[0][i]

        data_flop = []

        data_flop.append(data_cards[k * 2])

        data_flop.append(data_cards[k * 2 + 1])

        data_flop.append(data_cards[k * 2 + 2])

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
                    time.sleep(2)
                    t = bot_flop(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], data_flop, bet, prev_bet,
                                 data_chips[next_move], data_bets[next_move])

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0
                                a = hand_links[next_move * 2 - 3].create_image(18, 26,
                                                                               image=image_links_f[next_move * 2 - 3])
                                b = hand_links[next_move * 2 - 4].create_image(18, 26,
                                                                               image=image_links_f[next_move * 2 - 4])

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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

                if next_move == 1:
                    if prev_bet != 0 and data_chips[1] > prev_bet * 2:
                        slider.configure(from_=prev_bet * 2, to=data_chips[1])
                    elif data_chips[1] > prev_bet * 2:
                        slider.configure(from_=blind * 2, to=data_chips[1])
                    else:
                        slider.configure(from_=data_chips[1], to=data_chips[1])

                    temporary = -1

                    t = temporary
                    while t == -1:
                        time.sleep(1)
                        t = temporary
                    temporary = -1
                    if t == -4:
                        if data_chips[1] <= prev_bet:
                            t = -2
                        else:
                            t = slider.get()
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet - data_bets[1]
                        else:
                            t = data_chips[1]

                    if t == -3:
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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
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

        bank_temp += sum(data_bets)
        data_pots = exchange(data_pots, data_bets, data_ingame, k)

        ############################# TURN #########################
        btn_win_prob_turn = Button(window, text="show win \n probability", bg="black", fg="red",
                                   font=("Arial Bold", 14),
                                   command=lambda: win_p_func_turn())
        btn_win_prob.destroy()
        btn_win_prob_turn.place(width=100, height=50, x=0, y=220)
        bank_temp += sum(data_bets)

        pilImage = Image.open(card_texture[data_cards[k * 2 + 3]])
        image4 = ImageTk.PhotoImage(pilImage)
        imagesprite4 = t4.create_image(42, 53, image=image4)

        for i in range(1, k + 1):
            data_ingame[i] = data_pots[0][i]
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
                    time.sleep(2)
                    t = bot_turn(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], data_turn, bet, prev_bet,
                                 data_chips[next_move], data_bets[next_move])

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0
                                a = hand_links[next_move * 2 - 3].create_image(18, 26,
                                                                               image=image_links_f[next_move * 2 - 3])
                                b = hand_links[next_move * 2 - 4].create_image(18, 26,
                                                                               image=image_links_f[next_move * 2 - 4])

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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))
                    p_bet.configure(text=str(data_bets[1]))

                if next_move == 1:
                    if prev_bet != 0 and data_chips[1] > prev_bet * 2:
                        slider.configure(from_=prev_bet * 2, to=data_chips[1])
                    elif data_chips[1] > prev_bet * 2:
                        slider.configure(from_=blind * 2, to=data_chips[1])
                    else:
                        slider.configure(from_=data_chips[1], to=data_chips[1])
                    temporary = -1
                    t = temporary
                    while t == -1:
                        time.sleep(1)
                        t = temporary

                    temporary = -1
                    if t == -4:
                        if data_chips[1] <= prev_bet:
                            t = -2
                        else:
                            t = slider.get()
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet - data_bets[1]
                        else:
                            t = data_chips[1]
                    if t == -3:
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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
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


        bank_temp += sum(data_bets)
        data_pots = exchange(data_pots, data_bets, data_ingame, k)

        ############################# RIVER #########################

        btn_win_prob_turn.destroy()
        bank_temp += sum(data_bets)
        pilImage = Image.open(card_texture[data_cards[k * 2 + 4]])
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
                    time.sleep(2)
                    t = bot_reaver(data_cards[next_move * 2 - 2], data_cards[next_move * 2 - 1], data_reaver, bet, prev_bet,
                                   data_chips[next_move], data_bets[next_move])

                    if t == 0:
                        for j in range(1, k + 1):
                            if data_bets[j] > data_bets[next_move]:
                                data_ingame[next_move] = 0
                                a = hand_links[next_move * 2 - 3].create_image(18, 26,
                                                                               image=image_links_f[next_move * 2 - 3])
                                b = hand_links[next_move * 2 - 4].create_image(18, 26,
                                                                               image=image_links_f[next_move * 2 - 4])

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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))

                if next_move == 1:
                    if prev_bet != 0 and data_chips[1] > prev_bet * 2:
                        slider.configure(from_=prev_bet * 2, to=data_chips[1])
                    elif data_chips[1] > prev_bet * 2:
                        slider.configure(from_=blind * 2, to=data_chips[1])
                    else:
                        slider.configure(from_=data_chips[1], to=data_chips[1])

                    t = temporary
                    temporary = -1
                    while t == -1:
                        time.sleep(1)
                        t = temporary
                    if t == -4:
                        if data_chips[1] <= prev_bet:
                            t = -2
                        else:
                            t = slider.get()
                    if t == -2:
                        if prev_bet < data_chips[1]:
                            t = prev_bet - data_bets[1]
                        else:
                            t = data_chips[1]

                    if t == -3:
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
                    bank.configure(text="BANK: " + str(sum(data_bets) + bank_temp))
                    p_ch.configure(text="Your chips: " + str(data_chips[1]))

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

        bank_temp += sum(data_bets)
        data_pots = exchange(data_pots, data_bets, data_ingame, k)

        data_pots = after_exchange(data_pots, data_bets, data_ingame, k)

        hand_links = create_hand_links()

        for i in range(len(hand_links)):
            if data_pots[0][i//2 + 2] != 0:
                imagesprite228 = hand_links[i].create_image(20, 25, image=image_links[i])

        time.sleep(10)

        for i in range(len(hand_links)):
            hand_links[i] = card_texture_small[0]

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

```
