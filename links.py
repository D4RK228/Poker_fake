def create_hand_links():
    hand_links = []
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

    h9_1 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
    h9_1.place(x = 677, y = 333)

    pilImage = Image.open(card_texture_small[0])
    image9_2 = ImageTk.PhotoImage(pilImage)
    imagesprite9_2 = h9_2.create_image(18, 27, image=image9_2)

    pilImage = Image.open(card_texture[0])
    image7 = ImageTk.PhotoImage(pilImage)
    imagesprite7 = c2.create_image(42, 53, image=image7)

    h9_2 = Canvas(window, width=37, height=54, bg="green", borderwidth=-2)
    h9_2.place(x = 720, y = 333)
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
        images.append(Image.Tk.PhotoImage(Image.open(card_texture[data_cards[i]])))
    return images



