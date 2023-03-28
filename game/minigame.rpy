init python:

    renpy.music.register_channel("itms", "sfx", False)

    # набор типов карточек
    all_cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    # ширина и высота поля
    ww = 3
    hh = 3
    # сколько карточек можно открыть за 1 ход
    max_c = 2
    # размер текста в карточке для текстового режима
    card_size = 48
    # время, выделенное на прохождение
    max_time = 25
    # пауза перед тем, как карточки исчезнут
    wait = 0.5
    # режим карточек с изображениями, а не с текстом
    img_mode = True

    values_list = []
    temp = []
    # картинки-карточки
    for fn in renpy.list_files():
        if fn.startswith("images/card_") and fn.endswith((".png")):
            name = fn[12:-4]
            renpy.image("card " + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))
    
    if len(temp) > 1:
        all_cards = temp
    else:
        img_mode = False

    def cards_init():
        global values_list
        values_list = []
        while len(values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice(all_cards)
            for i in range(0, max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list)
        while len(values_list) < ww * hh:
            values_list.append('empty')

# экран игры
screen memo_scr:
    # таймер    
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    # поле
    grid ww hh:
        align (.5, .5)
        for card in cards_list:
            button:
                left_padding 10
                right_padding 10
                top_padding 10
                bottom_padding 10
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card empty"
                    else:
                        text " " size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card " + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card back"
                        else:
                            text "#" size card_size
                # нажатие на карточку
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
                
    text str(memo_timer) xalign .5 yalign 0.0 size card_size

    # renpy.play("sounds/for_cards.mp3", channel="itms")
    # Play("itms", "sounds/for_cards.mp3")

# сама игра
label memoria_game:
    scene black
    $ cards_init()
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            if values_list[i] == 'empty':
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":True} )   
            else:
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )   
    $ memo_timer = max_time
    
    show screen memo_scr

    # основной цикл игры
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        # предотвращение открытия лишних карточек
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause (wait, hard = True)
            python: 
                for i in range (0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memo_game_loop")
                renpy.jump ("memo_game_win")
        jump memo_game_loop

# проигрыш
label memo_game_lose:
    hide screen memo_scr
    hide screen info_panel

    $ renpy.pause (0.1, hard = True)

    scene bg wasted
    play sound lose

    centered " "

    jump memoria_game

# выигрыш
label memo_game_win:
    hide screen memo_scr
    hide screen info_panel

    $ renpy.pause (0.2, hard = True)

    scene bg passed
    play sound win

    centered " "

    return
