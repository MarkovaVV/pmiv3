# Музыка и звуки
define audio.main = "music/main.mp3"
define audio.lose = "sounds/wasted.mp3"
define audio.win = "sounds/level_up.mp3"


label start:
    scene black
    play music main

    $ max_time = 20
    $ ww, hh = 2, 3

    call memoria_game
    jump level_two


label level_two:
    scene black

    $ max_time = 20
    $ ww, hh = 4, 2

    call memoria_game
    jump level_three


label level_three:
    scene black

    $ max_time = 25
    $ ww, hh = 3, 4

    call memoria_game
    jump level_four


label level_four:
    scene black

    $ max_time = 30
    $ ww, hh = 4, 4

    call memoria_game
    jump level_five


label level_five:
    scene black

    $ max_time = 35
    $ ww, hh = 4, 5

    call memoria_game
    jump finish


label finish:
    scene black
    centered "{size=56}{b}Поздравляем!{/b}\n Вы прошли игру.{/size}"