"""
Created by: Jayden Okafor
Created on: Mar 2026
This program turns the servo to 0 when the button "A" is clicked and then turns the servo to 180 when the button "B" is clicked
"""

from microbit import *

# variable
servo = None

# show happy face
display.show(Image.HAPPY)


# library
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1 / self.freq) * 1000)
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(1000)
        self.pin.write_digital(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)


# assign pin 15 to the servo variable
servo = Servo(pin15)

while True:
    # when button a is pressed
    if button_a.was_pressed():
        display.clear()
        display.show("0")
        sleep(1000)
        display.show(Image.SQUARE_SMALL)
        sleep(600)
        servo.write_angle(0)
        display.show(Image.HAPPY)

    # when button b is pressed
    if button_b.was_pressed():
        display.clear()
        display.scroll("180")
        display.show(Image.SQUARE_SMALL)
        sleep(600)
        servo.write_angle(180)
        display.show(Image.HAPPY)
