"""
            presentationPointer (c) 2019 by Michał Stojke, LICENSE: MIT

	Simple code which allows to interpret received IR codes from Arduino UNO into PC 
	keyboard codes. Just run this code and PowerPoint and have fun! EKHM... if you 
	have a SAMSUNG TV REMOTE, otherwise you need to look at define section and change
	key codes accordingly to yours remote controller.

"""

import serial
import time
from pynput.keyboard import Key, Controller

# define section
com_port = 'COM6' # port on which Arduino is connected
baud_rate = '9600' # baud rate of connection
back_key = '-22951' # key code from remote which turn back slide
forward_key = '18105' # key code from remote which turn forward slide
f5_key = '5865' # key code from remote which turn on presentation mode
esc_key = '-19381' # key code from remote which turn of presentation mode (ESC key)

connection = serial.Serial(port=com_port, baudrate=baud_rate)
keyboard = Controller()

last_key = ''

while True:
		try:
			data = connection.readline()[:-1].decode("utf-8", "ignore").strip()
			print("Received IR code: {0}".format(data))
			if data == back_key:
				print('Clicked: Back Key')
				keyboard.press(Key.left)
			if data == forward_key:
				print('Clicked: Forward Key')
				keyboard.press(Key.right)
			if data == f5_key:
				print('Clicked: F5 Key')
				keyboard.press(Key.f5)
			if data == esc_key:
				print('Clicked: ESC Key')
				keyboard.press(Key.esc)
		except serial.SerialException as e:
			print("Disconnect of USB -> UART occured. \nRestart needed!")
			quit()
		except TypeError as e:
			print("ERROR")
			quit()

connection.close()
