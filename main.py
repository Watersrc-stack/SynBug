def Display_number(num: number):
    if num == 1:
        pass
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        pass
    elif num == 5:
        pass
    elif num == 6:
        pass
    elif num == 7:
        pass
    elif num == 8:
        pass
    elif num == 9:
        pass

ncanal = 0
canal_choiced = 0
while canal_choiced == 0:
    if input.button_is_pressed(Button.A) and ncanal >= 2:
        ncanal += -1
        Display_number(ncanal)
    elif input.button_is_pressed(Button.B) and ncanal <= 8:
        ncanal += 1
        Display_number(ncanal)
    elif input.button_is_pressed(Button.AB):
        canal_choiced = 1
radio.set_group(ncanal)