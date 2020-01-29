def texture_fill():
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
    return card_texture

def texture_small_fill():
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
    card_texture_small.append("rubashka-fold.jpg")
    return card_texture_small