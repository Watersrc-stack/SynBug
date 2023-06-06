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
music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 54, 54, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
images.createImage(`
    . . # # #
    . . . . .
    . # # # .
    . . . . .
    # # # . .
    `).showImage(0)
control.waitMicros(3000000)
clear_screen()
let ncanal = 3
Display_number(ncanal)
while (canal_choiced == 0) {
    if (input.buttonIsPressed(Button.AB)) {
        canal_choiced = 1
        Display_number(ncanal)
    } else if (input.buttonIsPressed(Button.A) && ncanal >= 2) {
        ncanal += -1
        Display_number(ncanal)
    } else if (input.buttonIsPressed(Button.B) && ncanal <= 8) {
        ncanal += 1
        Display_number(ncanal)
    } else {
    	
    }
}
radio.setGroup(ncanal)
music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.InBackground)
images.iconImage(IconNames.Yes).showImage(0)
control.waitMicros(2000000)
images.iconImage(IconNames.House).showImage(0)
