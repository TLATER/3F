# Write your code here :-)
from microbit import *
import utime
import microbit

n = 12
show_temp = True
show_setting = False

def current_temp():
    temp = temperature()
    display.show(str(temp)+('C'))

def wanted_temp(q):
    m = button_a.get_presses()
    q = q - m
    p = button_b.get_presses()
    q = q + p
    display.scroll(str(q)+('C'))

    return q

def fans_on():
    microbit.pin2.write_digital(1)

def fans_off():
    microbit.pin2.write_digital(0)

while True:
    c_temp = temperature()

    if c_temp >= n:
        fans_on()

        if show_temp and not show_setting:
            if button_a.was_pressed() or button_b.was_pressed():
                show_temp = False
                show_setting = True
                time1 = utime.ticks_ms()
            else:
                current_temp()

        if not show_temp and show_setting:
            timepass = 200
            time2 = time1 + timepass
            if utime.ticks_ms() >= time2:
                show_temp = True
                show_setting = False
            else:
                n = wanted_temp(n)

    else:
        display.scroll('NOW!')
        fans_off()