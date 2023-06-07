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
    if (receivedString == "JOIN" && players_lst.length > 0) {
        radio.sendValue("LENLST", players_lst.length)
        music.playTone(523, music.beat(BeatFraction.Whole))
    } else if (receivedString.includes("JOINLST")) {
        players_lst.push(receivedString.substr(7, 4))
        music.playTone(698, music.beat(BeatFraction.Whole))
    } else {
    	
    }
})
radio.onReceivedValue(function (name, value) {
    if (name == "LENLST") {
        radio.sendString("JOINLST" + id_player)
        in_list = 1
        music.playTone(311, music.beat(BeatFraction.Whole))
    }
})
let tmp = 0
let players_lst: string[] = []
let in_list = 0
let canal_choiced = 0
let id_player = ""
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
id_player = "" + id_chat_lst._pickRandom() + id_chat_lst._pickRandom() + id_chat_lst._pickRandom() + id_chat_lst._pickRandom()
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
in_list = 0
players_lst = []
while (in_list == 0) {
    if (input.buttonIsPressed(Button.AB)) {
        control.waitMicros(2000000)
        music.playTone(294, music.beat(BeatFraction.Whole))
        players_lst.push(id_player)
        images.iconImage(IconNames.Pitchfork).showImage(0)
        in_list = 1
        tmp = players_lst.length
    } else {
        radio.sendString("JOIN")
        music.ringTone(233)
        control.waitMicros(2000000)
    }
}
images.iconImage(IconNames.Diamond).showImage(0)
