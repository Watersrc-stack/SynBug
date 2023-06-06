let ncanal = 0
let canal_choiced = 0
while (canal_choiced == 0) {
    if (input.buttonIsPressed(Button.A) && ncanal >= 2) {
        ncanal += -1
    } else if (input.buttonIsPressed(Button.B) && ncanal <= 8) {
        ncanal += 1
    } else if (input.buttonIsPressed(Button.AB)) {
        canal_choiced = 1
    }
}
radio.setGroup(ncanal)
basic.forever(function () {
	
})
