# Joystick-Bit-Python
A way to use a Micro:Bit and a Joystick:Bit in a python project.
\
The Microbit.py file is for the Microsoft Makecode Editor

# Documention

First put the Controller Class in the Main.py in your code.

Initialize a Controller:
\
controller = Controller('YOUR COM PORT HERE', YOUR BAUDRATE HERE)

Get the data:
\
controller.Get_Data()

The data is stored in 3 varibles.
\
button = controller.Button
\
joystickX = controller.X
\
joystickY = controller.Y

To close the serial port:
\
controller.Close_Port()

To show some text on your microbit:
\
controller.Set_Text('YOUR TEXT HERE')
\
This only works once so only use this for a game title.
