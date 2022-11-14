import RPi.GPIO as GPIO
import time
import uinput
import os

GPIO.setmode(GPIO.BCM)
/*pin activeren*/
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

device = uinput.Device([
	uinput.KEY_P,
	uinput.KEY_N,
	uinput.KEY_F5,
	uinput.KEY_M,
	uinput.KEY_A,
	uinput.KEY_W,
	uinput.KEY_T,
	uinput.KEY_Tab
        ])
/*maandoverzicht als standaard zetten*/
view = 'm'
knopBack = True
knopMulti = True
knopForward = True

def knopStatus():
/*state van knoppen ophalen en in variabele zetten*/
	if input_state_back == False:
			knopBack = False
	if input_state_forward == False:
			knopForward = False
	if input_state_multi == False:
			knopMulti = False


while True:
/*pins mappen - van links naar rechts (middelste knop is multi knop*/
	input_state_back = GPIO.input(19)
	input_state_multi = GPIO.input(20)
	input_state_forward = GPIO.input(21)

knopStatus()
time.sleep(2)

	if knopMulti == False and knopBack == False and knopForward == False:
		print('All buttons pressed')
		knopBack = True
		knopForward = True
		knopMulti = True
		time.sleep(2)
		os.system('sudo reboot')

	if knopBack == False and knopForward == False:
		print('Refresh')
		device.emit_click(uinput.KEY_F5)
		knopBack = True
		knopForward = True

	if knopBack == False:
		print('Button P pressed')
		device.emit_click(uinput.KEY_P)
		knopBack = True

	if knopForward == False:
		print('Button F pressed')
		device.emit_click(uinput.KEY_F)
		knopForward = True




	if knopMulti == False:
		print('Multi button pressed')
		knopMulti = True
		
		if view == 'm':
			device.emit_click(uinput.KEY_W)
			view = 'w'
			print('Weekoverzicht gekozen')

		if view == 'w':
			device.emit_click(uinput.KEY_A)
			view = 'a'
			print('Gebeurtenissenlijst gekozen')

		elif:
			device.emit_click(uinput.KEY_M)
			view = 'm'
			print('Maandoverzicht gekozen')	


