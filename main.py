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
    if receivedString.index_of("JOIN") >= 0 and len(players_lst) > 0:
        players_lst.append(receivedString.slice(5))
        radio.send_string("CONFIRM")
    elif receivedString == "CONFIRM":
        in_list = 1
radio.on_received_string(on_received_string)

tmp = 0
players_lst: List[str] = []
in_list2 = 0
canal_choiced = 0
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
while in_list2 == 0:
    if input.button_is_pressed(Button.AB):
        control.wait_micros(2000000)
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        players_lst.append(id_player)
        images.icon_image(IconNames.PITCHFORK).show_image(0)
        in_list2 = 1
        tmp = len(players_lst)
    else:
        radio.send_string("JOIN " + id_player)
        music.ring_tone(233)
        control.wait_micros(2000000)
images.icon_image(IconNames.DIAMOND).show_image(0)