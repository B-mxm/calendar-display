import RPi.GPIO as GPIO
import time
import uinput
import os

GPIO.setmode(GPIO.BCM)
#pin activeren
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
	uinput.KEY_T        ])
#maandoverzicht als standaard zetten
view = 'm'

while True:
time.sleep(0.5)
#pins mappen - van links naar rechts (middelste knop is multi knop
    input_state_back = GPIO.input(19)
    input_state_multi = GPIO.input(20)
    input_state_forward = GPIO.input(21)

    if input_state_back == False:
        print('Button P Pressed')
        device.emit_click(uinput.KEY_P)
        time.sleep(0.5)
    if input_state_forward == False:
        print('Button N Pressed')
        device.emit_click(uinput.KEY_N)
        time.sleep(0.5)

    if input_state_multi == False and input_state_back == False and input_state_forward == False:
        print('All buttons pressed')
        os.system('sudo reboot')

    if input_state_multi == False:
	start = time.time_ns()
	time.sleep(0.01)
	while input_state_multi == False:
		time.sleep(0.01)
		print('Multibutton is pressed')
		end = time.time_ns()
		multi_press_time = end-start
		input_state_multi = GPIO.input(20)

		if input_state_multi ==  True or multi_press_time > 5.5:
			print('Button press in', multi_press_time)
			break


	if multi_press_time < 5:
        	if view == 'm':
			device.emit_click(uinput.KEY_W)
			view = 'w'
			print('keypress a')
			time.sleep(0.5)
		elif view == 'w':
			device.emit_click(uinput.KEY_A)
			view = 'a'
			print('keypress a')
			time.sleep(0.5)
		elif view == 'a':
			device.emit_click(uinput.KEY_M)
			view = 'm'
			print('keypress m')
			time.sleep(0.5)
		
	else:
		print('today')
		device.emit_click(uinput.KEY_T)
		time.sleep(0.5)

    if input_state_multi == False and input_state_back == False and input_state_forward == False:
	print('All buttons pressed')
	os.system('sudo reboot')

    if input_state_forward == False and input_state_back == False:
 	print ('refresh F5')
	device.emit_click(uinput.KEY_F5)
