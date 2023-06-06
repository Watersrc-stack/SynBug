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
    else:
        pass
radio.set_group(ncanal)