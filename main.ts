function Display_number (num: number) {
    if (num == 1) {
        images.createImage(`
            # # # . .
            . . # . .
            . . # . .
            . . # . .
            # # # # #
            `).showImage(0)
    } else if (num == 2) {
        images.createImage(`
            # # # # #
            . . . . #
            # # # # #
            # . . . .
            # # # # #
            `).showImage(0)
    } else if (num == 3) {
        images.createImage(`
            . # # # .
            # . . . #
            . . # # .
            # . . . #
            . # # # .
            `).showImage(0)
    } else if (num == 4) {
        images.createImage(`
            # . . . #
            # . . . #
            # # # # #
            . . . . #
            . . . . #
            `).showImage(0)
    } else if (num == 5) {
        images.createImage(`
            # # # # #
            # . . . .
            # # # # #
            . . . . #
            # # # # #
            `).showImage(0)
    } else if (num == 6) {
        images.createImage(`
            # # # # #
            # . . . .
            # # # # #
            # . . . #
            # # # # #
            `).showImage(0)
    } else if (num == 7) {
        images.createImage(`
            # # # # #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `).showImage(0)
    } else if (num == 8) {
        images.createImage(`
            # # # # #
            # . . . #
            . # # # .
            # . . . #
            # # # # #
            `).showImage(0)
    } else if (num == 9) {
        images.createImage(`
            # # # # #
            # . . . #
            # # # # #
            . . . . #
            # # # # #
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
radio.onReceivedString(function (receivedString) {
    let in_list: number;
if (receivedString.indexOf("JOIN") >= 0 && players_lst.length > 0) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        players_lst.push(receivedString.slice(5))
        radio.sendString("CONFIRM")
    } else if (receivedString == "CONFIRM") {
        music.playTone(659, music.beat(BeatFraction.Whole))
        in_list2 = 1
    }
})
let tmp = 0
let players_lst: string[] = []
let in_list2 = 0
let canal_choiced = 0
music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 54, 54, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
images.createImage(`
    . . # # #
    . . . . .
    . # # # .
    . . . . .
    # # # . .
    `).showImage(0)
let id_chat_lst = [
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h"
]
let id_player = "" + id_chat_lst._pickRandom() + id_chat_lst._pickRandom() + id_chat_lst._pickRandom() + id_chat_lst._pickRandom()
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
in_list2 = 0
while (in_list2 == 0) {
    if (input.buttonIsPressed(Button.AB)) {
        control.waitMicros(2000000)
        music.playTone(294, music.beat(BeatFraction.Whole))
        players_lst.push(id_player)
        images.iconImage(IconNames.Pitchfork).showImage(0)
        in_list2 = 1
        tmp = players_lst.length
    } else if (input.buttonIsPressed(Button.A)) {
    	
    } else if (input.buttonIsPressed(Button.B)) {
    	
    } else {
    	
    }
    radio.sendString("JOIN " + id_player)
    control.waitMicros(2000000)
}
music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 500, 499, 255, 0, 750, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
images.iconImage(IconNames.Diamond).showImage(0)
