def button():
    global buttonVal, item
    buttonVal = pins.analog_read_pin(AnalogPin.P2)
    if buttonVal < 256:
        item = 1
    elif buttonVal < 597:
        item = 2
    elif buttonVal < 725:
        item = 3
    elif buttonVal < 793:
        item = 4
    elif buttonVal < 836:
        item = 5
    elif buttonVal < 938:
        item = 6
    else:
        item = 0
Y = 0
X = 0
item = 0
buttonVal = 0
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)

def on_forever():
    basic.show_string(serial.read_string())
    basic.pause(200)
basic.forever(on_forever)

def on_forever2():
    global X, Y
    button()
    if pins.analog_read_pin(AnalogPin.P0) < 400:
        X = -1
    elif pins.analog_read_pin(AnalogPin.P0) > 600:
        X = 1
    else:
        X = 0
    if pins.analog_read_pin(AnalogPin.P1) < 400:
        Y = -1
    elif pins.analog_read_pin(AnalogPin.P1) > 600:
        Y = 1
    else:
        Y = 0
    serial.write_numbers([X, Y, item])
basic.forever(on_forever2)
