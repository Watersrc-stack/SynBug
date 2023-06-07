def Display_number(num: number):
    if num == 1:
        images.create_image("""
            # # # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        # # # # #
        """).show_image(0)
    elif num == 2:
        images.create_image("""
            # # # # #
                        . . . . #
                        # # # # #
                        # . . . .
                        # # # # #
        """).show_image(0)
    elif num == 3:
        images.create_image("""
            . # # # .
                        # . . . #
                        . . # # .
                        # . . . #
                        . # # # .
        """).show_image(0)
    elif num == 4:
        images.create_image("""
            # . . . #
                        # . . . #
                        # # # # #
                        . . . . #
                        . . . . #
        """).show_image(0)
    elif num == 5:
        images.create_image("""
            # # # # #
                        # . . . .
                        # # # # #
                        . . . . #
                        # # # # #
        """).show_image(0)
    elif num == 6:
        images.create_image("""
            # # # # #
                        # . . . .
                        # # # # #
                        # . . . #
                        # # # # #
        """).show_image(0)
    elif num == 7:
        images.create_image("""
            # # # # #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """).show_image(0)
    elif num == 8:
        images.create_image("""
            # # # # #
                        # . . . #
                        . # # # .
                        # . . . #
                        # # # # #
        """).show_image(0)
    elif num == 9:
        images.create_image("""
            # # # # #
                        # . . . #
                        # # # # #
                        . . . . #
                        # # # # #
        """).show_image(0)
def clear_screen():
    images.create_image("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """).show_image(0)

def on_received_string(receivedString):
    if receivedString == "JOIN" and len(players_lst) > 0:
        radio.send_value("LENLST", len(players_lst))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
    elif receivedString.includes("JOINLST"):
        players_lst.append(receivedString.substr(7, 4))
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
    else:
        pass
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    global in_list
    clear_screen()
    if name == "LENLST" and value > 0:
        radio.send_string("JOINLST" + id_player)
        in_list = 1
        music.play_tone(554, music.beat(BeatFraction.WHOLE))
radio.on_received_value(on_received_value)

tmp = 0
players_lst: List[str] = []
in_list = 0
canal_choiced = 0
id_player = ""
music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
        54,
        54,
        255,
        0,
        500,
        SoundExpressionEffect.NONE,
        InterpolationCurve.LINEAR),
    SoundExpressionPlayMode.IN_BACKGROUND)
images.create_image("""
    . . # # #
        . . . . .
        . # # # .
        . . . . .
        # # # . .
""").show_image(0)
id_chat_lst = ["a", "b", "c", "d", "e", "f", "g", "h"]
id_player = "" + id_chat_lst._pick_random() + id_chat_lst._pick_random() + id_chat_lst._pick_random() + id_chat_lst._pick_random()
control.wait_micros(3000000)
clear_screen()
ncanal = 3
Display_number(ncanal)
while canal_choiced == 0:
    if input.button_is_pressed(Button.AB):
        canal_choiced = 1
        Display_number(ncanal)
    elif input.button_is_pressed(Button.A) and ncanal >= 2:
        ncanal += -1
        Display_number(ncanal)
    elif input.button_is_pressed(Button.B) and ncanal <= 8:
        ncanal += 1
        Display_number(ncanal)
    else:
        pass
radio.set_group(ncanal)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
    SoundExpressionPlayMode.IN_BACKGROUND)
images.icon_image(IconNames.YES).show_image(0)
control.wait_micros(2000000)
images.icon_image(IconNames.HOUSE).show_image(0)
in_list = 0
players_lst = []
while in_list == 0:
    if input.button_is_pressed(Button.AB):
        control.wait_micros(2000000)
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        players_lst.append(id_player)
        images.icon_image(IconNames.PITCHFORK).show_image(0)
        in_list = 1
        tmp = len(players_lst)
    else:
        radio.send_string("JOIN")
        control.wait_micros(2000000)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.twinkle),
    SoundExpressionPlayMode.IN_BACKGROUND)
images.icon_image(IconNames.DIAMOND).show_image(0)