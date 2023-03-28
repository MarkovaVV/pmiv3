# Музыка и звуки
define audio.main = "music/main.mp3"
define audio.lose = "sounds/wasted.mp3"
define audio.win = "sounds/level_up.mp3"

define f = Character('Фумо №1', color="#df0d76")

define k = 1

screen info_panel:
    frame:
        padding(10, 10)
        xalign 0.5
        yalign 0.07
        text "Уровень [k]"

label start:
    scene black
    
    show fumo:
        xalign 0.03
        yalign 0.6

    f '''
    Здравствуй, мой дорогой друг!
    {w} Ты попал на игру "Найди Фумо".

    Эта игра более известна в России под названием Найди пару.
    {w} Тебе прийдется пройти пять уровней.

    Суть игры очень простая. 
    
    Даны карточки, которые выкладываются «рубашкой» вверх. 
    {w} Далее вы открываете две любые карточки. 
    {w} Если на них изображены одинаковые Фумо, то карточки исчезают, и вы вскрываете следующую пару. 

    Однако, если изображения разные, то карточки возвращаются в режим «рубашкой вверх». 
    {w} Когда все карточки будут разобраны, вы переходите на другой уровень.

    Ой! {w} Чуть ни забыла. Вы должны будете успеть сделать это за определенное время. 
    {w} Каждый уровень все сложнее и сложнее, чтобы было веселее!

    Вот и все! Очень-очень просто. 

    Желаю Вам удачи, мой дорогой друг!
    '''

    jump level_one


label level_one:
    scene black
    play music main

    show screen info_panel

    $ max_time = 20
    $ ww, hh = 2, 3

    call memoria_game
    jump level_two


label level_two:
    scene black

    $ k += 1
    show screen info_panel

    $ max_time = 20
    $ ww, hh = 4, 2

    call memoria_game
    jump level_three


label level_three:
    scene black

    $ k += 1
    show screen info_panel

    $ max_time = 25
    $ ww, hh = 3, 4

    call memoria_game
    jump level_four


label level_four:
    scene black

    $ k += 1
    show screen info_panel

    $ max_time = 30
    $ ww, hh = 4, 4

    call memoria_game
    jump level_five


label level_five:
    scene black

    $ k += 1
    show screen info_panel

    $ max_time = 35
    $ ww, hh = 4, 5

    call memoria_game
    jump finish


label finish:
    scene black
    centered "{size=80}{b}Поздравляем!{/b}\n\n Вы прошли игру.{/size}"