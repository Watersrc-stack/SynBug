class Test:
    def __init__(self):
        self.state = True

def Display_number(num: number):
    if num == 1:
        images.create_image("""
            . . # . .
                        . # # . .
                        # . # . .
                        . . # . .
                        . . # . .
        """).show_image(0)
    elif num == 2:
        images.create_image("""
            . # # # .
                        # . . . #
                        . . . # .
                        . . # . .
                        . # # # #
        """).show_image(0)
    elif num == 3:
        images.create_image("""
            . # # . .
                        . . . # .
                        . . # . .
                        . . . # .
                        . # # . .
        """).show_image(0)
    elif num == 4:
        images.create_image("""
            . . # . .
                        . # . . .
                        # . . # .
                        . # # # #
                        . . . # .
        """).show_image(0)
    elif num == 5:
        images.create_image("""
            . # # # .
                        . # . . .
                        . . # . .
                        . . . # .
                        . # # . .
        """).show_image(0)
    elif num == 6:
        images.create_image("""
            . . # # .
                        . # . . .
                        . . # # .
                        . # . . #
                        . . # # .
        """).show_image(0)
    elif num == 7:
        images.create_image("""
            . # # # .
                        . . . # .
                        . . # . .
                        . . # . .
                        . # . . .
        """).show_image(0)
    elif num == 8:
        images.create_image("""
            . . # # .
                        . # . . #
                        . . # # .
                        . # . . #
                        . . # # .
        """).show_image(0)
    elif num == 9:
        images.create_image("""
            . . # # .
                        . # . . #
                        . . # # #
                        . . . # .
                        . . # . .
        """).show_image(0)
def clear_screen():
    images.create_image("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """).show_image(0)
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
control.wait_micros(3000000)
clear_screen()
ncanal = 3
Display_number(ncanal)
while canal_choiced == 0:
    if input.button_is_pressed(Button.A) and ncanal >= 2:
        ncanal += 0 - 1
        Display_number(ncanal)
    elif input.button_is_pressed(Button.B) and ncanal <= 8:
        ncanal += 1
        Display_number(ncanal)
    elif input.button_is_pressed(Button.AB):
        canal_choiced = 1
        Display_number(ncanal)
    else:
        pass
radio.set_group(ncanal)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
    SoundExpressionPlayMode.IN_BACKGROUND)
images.icon_image(IconNames.YES).show_image(0)
control.wait_micros(2000000)
images.icon_image(IconNames.HOUSE).show_image(0)