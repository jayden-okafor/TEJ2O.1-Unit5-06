/* Copyright (c) 2026 MTHS All rights reserved
 *
 * Created by: Jayden Okafor
 * Created on: Mar 2026
 * This program turns the servo to 0 when the button "A" is clicked and then turns the servo to 180 when the button "B" is clicked
*/

// variables
const servoNumber8 = robotbit.Servos.S8

// show hapy face
basic.showIcon(IconNames.Happy)

// when button "A" is clicked
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    robotbit.Servo(servoNumber8, 0)
    basic.showString('0')
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.Happy)
})

input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    robotbit.Servo(servoNumber8, 180)
    basic.showString('180')
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.Happy)
})
