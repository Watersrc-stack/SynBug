function Display_number (num: number) {
    if (num == 1) {
        images.createImage(`
            . . # . .
            . # # . .
            # . # . .
            . . # . .
            . . # . .
            `).showImage(0)
    } else if (num == 2) {
        images.createImage(`
            . # # # .
            # . . . #
            . . . # .
            . . # . .
            . # # # #
            `).showImage(0)
    } else if (num == 3) {
        images.createImage(`
            . # # . .
            . . . # .
            . . # . .
            . . . # .
            . # # . .
            `).showImage(0)
    } else if (num == 4) {
        images.createImage(`
            . . # . .
            . # . . .
            # . . # .
            . # # # #
            . . . # .
            `).showImage(0)
    } else if (num == 5) {
        images.createImage(`
            . # # # .
            . # . . .
            . . # . .
            . . . # .
            . # # . .
            `).showImage(0)
    } else if (num == 6) {
        images.createImage(`
            . . # # .
            . # . . .
            . . # # .
            . # . . #
            . . # # .
            `).showImage(0)
    } else if (num == 7) {
        images.createImage(`
            . # # # .
            . . . # .
            . . # . .
            . . # . .
            . # . . .
            `).showImage(0)
    } else if (num == 8) {
        images.createImage(`
            . . # # .
            . # . . #
            . . # # .
            . # . . #
            . . # # .
            `).showImage(0)
    } else if (num == 9) {
        images.createImage(`
            . . # # .
            . # . . #
            . . # # #
            . . . # .
            . . # . .
            `).showImage(0)
    }
}
function clear_screen () {
    images.createImage(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `).showImage(0)
}
let canal_choiced = 0
let ncanal = 3
while (canal_choiced == 0) {
    if (input.buttonIsPressed(Button.A) && ncanal >= 2) {
        ncanal += -1
        Display_number(ncanal)
    } else if (input.buttonIsPressed(Button.B) && ncanal <= 8) {
        ncanal += 1
        Display_number(ncanal)
    } else if (input.buttonIsPressed(Button.AB)) {
        canal_choiced = 1
    }
}
radio.setGroup(ncanal)
